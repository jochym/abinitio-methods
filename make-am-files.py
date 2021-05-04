#!/usr/bin/env python3

import sys
import ase.io
import spglib
import click
from collections import OrderedDict

@click.command()
@click.argument('action', default='gen')
@click.option('-o', '--order', default=1, help='Approximation order (1)')
@click.option('-p', '--prefix', default='CRYST', help='Prefix used in calculations (CRYST)')
@click.option('-n', '--name', default='SPOSCAR', type=click.Path(exists=True), help='Supercell POSCAR file (SPOSCAR)')
@click.option('-s', '--scale', default=1.0, help='Scale of the unit cell (1.0)')
@click.option('-e', '--evec', default=1, help='Print eigenvectors (1)')
@click.option('-m', '--msd', default=1, help='Print mean squere displacement (1)')
@click.option('--c1', default='None', type=str, help='First order interaction cutoff (None)')
@click.option('--c2', default='10', type=str, help='Second order interaction cutoff (10)')
@click.option('--c3', default='10', type=str, help='Third order interaction cutoff (10)')
@click.option('-k', '--kpath', default=None, type=click.Path(exists=True), help='File with reciprocal space path')
@click.option('-g', '--grid', default='10x10x10', help='k-grid for dos calculation (10x10x10)')
@click.option('-d', '--ndat', default=0, help='Number of data points used in fitting (All)', type=int)
@click.option('-f', '--dfset', default='DFSET', help='Name of the DFSET file (DFSET)')
@click.option('-t', '--tmax', default=1000, help='Max temperature (1000)')
@click.option('-c', '--charge', default=None, help='Name of the Born effective charges file (<prefix>.born)')
@click.option('-b', '--born', default=0, help='If non-zero use info from <prefix>.born as Born effective charges.' + 
                                              ' Use <born> = [1,2,3] value to select method of non-analytic correction.')
def gen(name, order, prefix, scale, action, evec, msd, tmax, charge, born, ndat, kpath, grid, c1, c2, c3, dfset):
    """Generates gen/opt/phon/dos file depending on the ACTION: gen (default, generate displacements), 
       opt (find force matrices), phon (calculate phonons), dos (calculate dos). 
       The default values of parameters are enclosed in parethesis.
    """

    tmpl={'gen':
'''
&general
  PREFIX = {prefix}
  MODE = {mode}
  NAT = {nat}
  NKD = {nkd}
  KD = {kd}
/

{dfset}

&interaction
  NORDER = {order}  # 1: harmonic, 2: cubic, ..
/

&cell
  {scale:14.10f} # units factor 
  {cell} # cell matrix
/

&cutoff 
  {cutoff}
/

&position
  {positions}
/
''',
          'phon':
'''
&general
  PREFIX = {prefix}
  MODE = {mode} ;   
  FCSXML = {prefix}.xml 
  NKD = {nkd}
  KD = {kd}
  MASS = {mass}
  TMAX = {tmax}
  EMIN = 0; EMAX = 1500; DELTA_E = 2
  {born}
/


&cell
  {scale:14.10f} # units factor 
  {cell} # cell matrix
/


&analysis
  PRINTMSD = {msd}
  PRINTEVEC = {evec}
  PDOS = 1
/

&kpoint
  {KMODE}
{KPATH}
/

'''}


    cr = ase.io.read(name)
    mode = ''
    NDATA = ''
    KMODE = 1
    KPATH = '10 10 10'
    
    cell = cr.get_cell()
    if action in ['dos','rta']:
        KMODE = 2
        KPATH = ' '.join(grid.split('x'))
    if action == 'phon':
        KMODE = 1
        if kpath is not None:
            with open(kpath) as kpf:
                KPATH = ''.join(kpf.readlines())
        else :
            print('No k-path given. Using Gamma-X.', file=sys.stderr)
            KPATH = 'G 0.0 0.0 0.0   X 0.0 0.5 0.0   51'
    if action in ['phon','dos','rta']:
        cell=spglib.find_primitive(cr)[0]
        mode = {'phon':'phonons', 'dos':'phonons', 'rta':'RTA'}[action]
        action='phon'
    if action == 'opt':
        if ndat > 0:
            NDATA = f'NDATA = {ndat}'
        dfset = f'&optimize\n  DFSET = {dfset}\n  {NDATA}\n/\n'
    else :
        dfset = ''
    if action in ['gen','opt']:
        mode = {'gen':'suggest', 'opt':'optimize'}[action]
        action = 'gen'
        
    


    cell = '\n  '.join([' '.join(['%14.10f' % c for c in v]) for v in cell])
    
    nat = len(cr.get_atomic_numbers())
    nkd = len(set(cr.get_atomic_numbers()))
    kd = ' '.join(list(OrderedDict.fromkeys(cr.get_chemical_symbols())))
    scl = 1.889725989*scale # in A -> bohr
    elems = {e:n+1 for n, e in enumerate(kd.split())}
    masses = {e:m for e,m in zip(cr.get_chemical_symbols(), cr.get_masses())}
    
    positions='\n  '.join(['{:d} {:14.10f} {:14.10f} {:14.10f}'.format(elems[e], p[0], p[1], p[2])
        for e, p in zip(cr.get_chemical_symbols(),cr.get_scaled_positions())])
    
    elm=kd.split()
    cutoff='\n  '.join(['{}-{} {}'.format(a,b, ' '.join([f'{c1}', f'{c2}', f'{c3}'][:order])) 
                        for k,a in enumerate(elm) for l,b in enumerate(elm) if k<=l])
    
    mass = ' '.join(['{:14.10f}'.format(masses[e]) for e in kd.split()])
    
    if born :
        if charge is None:
            charge=prefix
        born = 'BORNINFO = {charge}.born \n  NONANALYTIC = {born} \n'.format(born=born, charge=charge)
    else :
        born = ''

    print(tmpl[action].format(prefix=prefix, nat=nat, nkd=nkd, kd=kd, order=order, evec=evec, msd=msd,
                              scale=scl, cell=cell, cutoff=cutoff, positions=positions, mass=mass, tmax=tmax, 
                              born=born, mode=mode, dfset=dfset, KMODE=KMODE, KPATH=KPATH))
    
if __name__ == '__main__':
    gen()
