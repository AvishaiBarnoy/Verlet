# -*- coding: utf-8 -*-
"""
Created on Thu Oct 27 12:23:43 2016

@author: OWNER
"""
mass = 39.948 # g/mol
epsilon = 0.0661 # j/mol
sigma = 0.3345 # nm

def lj_pot():
    r = input('Enter inter-atomic distance?',)
    r = float(r)
    V = round(4*epsilon*((sigma/r)**12-(sigma/r)**6),12)
    return 'V = ' + str(V)
    
print(lj_pot())

