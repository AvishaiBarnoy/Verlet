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

from math import sqrt

def get_distances(coord):
    dis = []
    for i in range(len(coord)):
        dis1 = []
        for j in range(len(coord)):
            d = sqrt((coord[i][0]-coord[j][0])**2+(coord[i][1]-coord[j][1])**2+(coord[i][2]-coord[j][2])**2)
            dis1.append(d)
        dis.append(dis1)
    return dis

#print(get_distances([[3,3,3],[0,0,0],[0,0,0]]))
    
def main():
    :"Natoms = read_Natoms()
#    mass = read_atom_mass(Natoms)
    coord = read_atom_coord(Natoms)
    distances = get_distances(coord)
#    print(mass)
#    print(coord)
    for d in distances:
        print(d)

#main()