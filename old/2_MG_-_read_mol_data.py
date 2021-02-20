# -*- coding: utf-8 -*-
"""
Created on Thu Oct 27 12:23:43 2016

@author: OWNER
"""
    
#print(lj_pot())

def read_Natoms():
    n = input('Number of atoms?')
    n = int(n)
    return n
#print(read_Natoms())  
  
def read_atom_mass(n):
    mass = []
    print('For each atom: mass', end=''),
    for i in range(n):
        m = input('')
        m = float(m)
        mass.append(m)
    return mass
#print(read_atom_mass(3))

def read_atom_coord(n):
    '''
    reads an integer n and and asks user to enter
    coordinates for each atome with a space between them
    '''
    coord = []
    print('For each atom: x, y, z', end='')
    for atom in range(n):
        coord1 = [] # coordinate of every atom
        coord1 = list(map(float,input().split(" ")))
        coord.append(coord1)
    #coord = np.array(coord)
    return coord

def main():
    Natoms = read_Natoms()
    mass = read_atom_mass(Natoms)
    coord = read_atom_coord(Natoms)
    print(mass)
    print(coord)


main()