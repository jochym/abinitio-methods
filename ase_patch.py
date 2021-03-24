#!/usr/bin/env python3

import re
import numpy as np

def read_abinit_out(fd):
    from ase.io.abinit import consume_multiline, read_stress
    from ase import Atoms
    from ase.units import Hartree, Bohr
    results = {}

    def skipto(string):
        for line in fd:
            if string in line:
                return line
        raise RuntimeError('Not found: {}'.format(string))

    line = skipto('Version')
    m = re.match(r'\.*?Version\s+(\S+)\s+of ABINIT', line)
    assert m is not None
    version = m.group(1)
    results['version'] = version

    use_v9_format = int(version.split('.', 1)[0]) >= 9

    shape_vars = {}

    skipto('echo values of preprocessed input variables')

    for line in fd:
        if '===============' in line:
            break

        tokens = line.split()
        if not tokens:
            continue

        for key in ['natom', 'nkpt', 'nband', 'ntypat']:
            if tokens[0] == key:
                shape_vars[key] = int(tokens[1])

        if line.lstrip().startswith('typat'):  # Avoid matching ntypat
            types = consume_multiline(fd, line, shape_vars['natom'], int)

        if 'znucl' in line:
            znucl = consume_multiline(fd, line, shape_vars['ntypat'], float)

        if 'rprim' in line:
            cell = consume_multiline(fd, line, 9, float)
            cell = cell.reshape(3, 3)

    natoms = shape_vars['natom']

    # Skip ahead to results:
    for line in fd:
        if 'was not enough scf cycles to converge' in line:
            raise RuntimeError(line)
        if 'iterations are completed or convergence reached' in line:
            break
    else:
        raise RuntimeError('Cannot find results section')

    def read_array(fd, nlines):
        arr = []
        for i in range(nlines):
            line = next(fd)
            arr.append(line.split()[1:])
        arr = np.array(arr).astype(float)
        return arr

    if use_v9_format:
        energy_header = '--- !EnergyTerms'
        total_energy_name = 'total_energy_eV'

        def parse_energy(line):
            return float(line.split(':')[1].strip())
    else:
        energy_header = 'Components of total free energy (in Hartree) :'
        total_energy_name = '>>>>>>>>> Etotal'

        def parse_energy(line):
            return float(line.rsplit('=', 2)[1]) * Hartree
    
    for line in fd:
        if 'cartesian coordinates (angstrom) at end' in line:
            positions = read_array(fd, natoms)
        if 'cartesian forces (eV/Angstrom) at end' in line:
            results['forces'] = read_array(fd, natoms)
        if 'Cartesian components of stress tensor (hartree/bohr^3)' in line:
            results['stress'] = read_stress(fd)
        
        if line.strip() == energy_header:
            # Header not to be confused with EnergyTermsDC,
            # therefore we don't use .startswith()
            energy = None
            for line in fd:
                # Which of the listed energies should we include?
                if total_energy_name in line:
                    energy = parse_energy(line)
                    break
            if energy is None:
                raise RuntimeError('No energy found in output')
            results['energy'] = results['free_energy'] = energy

        if 'END DATASET(S)' in line:
            break

    for line in fd:
        if 'outvars: echo values of variables after computation' in line:
            break

    acell = np.ones(3)
    for line in fd:
        if 'acell' in line:
            tokens = line.lower().split()
            unit = 1.0
            index = tokens.index("acell")
            if(tokens[index + 4][:3] != 'ang'):
                unit = Bohr
            acell = np.array([unit * float(tokens[index + 1]),
                              unit * float(tokens[index + 2]),
                              unit * float(tokens[index + 3])])
            #print(acell)

        if 'rprim' in line:
            cell = consume_multiline(fd, line, 9, float)
            cell = acell[:,None]*cell.reshape(3, 3)
            #print(cell)

        if 20*'=' in line:
            break
                       
    znucl_int = znucl.astype(int)
    znucl_int[znucl_int != znucl] = 0  # (Fractional Z)
    numbers = znucl_int[types - 1]

    atoms = Atoms(numbers=numbers,
                  positions=positions,
                  cell=cell,
                  pbc=True)

    results['atoms'] = atoms
    return results

