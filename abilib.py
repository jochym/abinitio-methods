#!/usr/bin/env python3

# (C) 2024 by Paweł T. Jochym
# License: CC-by-SA 4.0

'''
This is a library of support functions for the "AbInitio Methods in Solid State Physics".
These functions may be used in other projects as well
'''

from ase.calculators.abinit import Abinit
from ase import units as un
import numpy as np

def set_params(calc, **args):
    '''
    Create new calculator with modified parameters based on the `calc` argument.
    '''
    params = dict(calc.parameters)
    for k, v in args.items():
        params[k] = v
    return Abinit(directory=calc.directory, **params)


def scan_param(cryst, param, start=0, stop=1, steps=7, 
               lista=None, log_scale=True, int_par=False):
    '''
    Scan a range of parameter param and plot 
    '''
    fi = lambda x: x
    fo = lambda x: x

    if lista is None:
        if log_scale :
            fi = np.log
            fo = np.exp
        lst = np.linspace(fi(start), fi(stop), steps)
    else :
        int_par=False
        lst = lista
    
    dat = []
    vs = []

    for v in lst:
        print(f'{param}=', end='')
        if lista is None:
            print(f'{int(fo(v)):<8d}' if int_par else f'{fo(v):<8.2f}', end=': ')
        else:
            print(f'{fo(v)}', end=': ')
        if int_par:
            cryst.calc = set_params(cryst.calc, **{param: int(fo(v))})
        else :
            cryst.calc = set_params(cryst.calc, **{param: fo(v)})
        vs.append(fo(v))
        dat.append([cryst.get_potential_energy(),
                    cryst.get_stress()[:3].mean()])
        print(f'{dat[-1][0]:.3f} eV ; {dat[-1][1]/un.GPa:6.3f} GPa',)
    dat = np.array(dat).T
    return vs, dat

