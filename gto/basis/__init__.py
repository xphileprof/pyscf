#!/usr/bin/env python
# -*- coding: utf-8
# Author: Qiming Sun <osirpt.sun@gmail.com>

import os
import imp
import pyscf.gto.basis.parse_nwchem
from pyscf.gto.basis.parse_nwchem import parse_str as parse

def load(basis_name, symb):
    # dict to map the basis name and basis file
    alias = {
        'ano'        : 'ano.dat'        ,
        'ccpv5z'     : 'cc-pv5z.dat'    ,
        'ccpvdz'     : 'cc-pvdz.dat'    ,
        'augccpvdz'  : 'aug-cc-pvdz.dat',
        'ccpvqz'     : 'cc-pvqz.dat'    ,
        'augccpvqz'  : 'aug-cc-pvqz.dat',
        'ccpvtz'     : 'cc-pvtz.dat'    ,
        'augccpvtz'  : 'aug-cc-pvtz.dat',
        'dyalldz'    : 'dyall_dz'       ,
        'dyallqz'    : 'dyall_qz'       ,
        'dyalltz'    : 'dyall_tz'       ,
        'faegredz'   : 'faegre_dz'      ,
        'iglo'       : 'iglo3'          ,
        'iglo3'      : 'iglo3'          ,
        '321g'       : '3-21g.dat'      ,
        '431g'       : '4-31g.dat'      ,
        '631g'       : '6-31g.dat'      ,
        '631gs'      : '6-31gs.dat'     ,
        '6311g'      : '6-311g.dat'     ,
        '6311gs'     : '6-311gs.dat'    ,
        '6311gsp'    : '6-311gsp.dat'   ,
        '6311gps'    : '6-311gsp.dat'   ,
        '321g'       : '3-21g.dat'      ,
        '431g'       : '4-31g.dat'      ,
        '631g'       : '6-31g.dat'      ,
        '631g*'      : '6-31gs.dat'     ,
        '6311g'      : '6-311g.dat'     ,
        '6311g*'     : '6-311gs.dat'    ,
        '6311g*+'    : '6-311gsp.dat'   ,
        '6311g+*'    : '6-311gsp.dat'   ,
        'sto3g'      : 'sto-3g.dat'     ,
        'sto6g'      : 'sto-6g.dat'     ,
        'minao'      : 'minao'          ,
        'dzpdunning' : 'dzp_dunning'    ,
        'dzp'        : 'dzp.dat'        ,
        'tzp'        : 'tzp.dat'        ,
        'qzp'        : 'qzp.dat'        ,
        'def2svp'    : 'def2-svp.dat'   ,
        'def2svpd'   : 'def2-svpd.dat'  ,
        'def2qzvpd'  : 'def2-qzvpd.dat' ,
        'def2qzvppd' : 'def2-qzvppd.dat',
        'def2qzvpp'  : 'def2-qzvpp.dat' ,
        'def2qzvp'   : 'def2-qzvp.dat'  ,
        'def2tzvpd'  : 'def2-tzvpd.dat' ,
        'def2tzvppd' : 'def2-tzvppd.dat',
        'def2tzvpp'  : 'def2-tzvpp.dat' ,
        'def2tzvp'   : 'def2-tzvp.dat'  ,
        'weigend'    : 'weigend_cfit.dat',
        'demon'      : 'demon_cfit.dat' ,
        'ahlrichs'   : 'ahlrichs_cfit.dat',
    }
    name = basis_name.lower().replace(' ', '').replace('-', '').replace('_', '')
    basmod = alias[name]
    symb = ''.join(i for i in symb if not i.isdigit())
    if 'dat' in basmod:
        b = parse_nwchem.parse(os.path.join(os.path.dirname(__file__), basmod), symb)
    else:
        fp, pathname, description = imp.find_module('minao', __path__)
        mod = imp.load_module(name, fp, pathname, description)
        #mod = __import__(basmod, globals={'__path__': __path__, '__name__': __name__})
        b = mod.__getattribute__(symb)
    return b

