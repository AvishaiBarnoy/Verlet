# -*- coding: utf-8 -*-
"""
Created on Thu Oct 27 12:23:43 2016

@author: OWNER
"""
mass = 39.948 # g/mol
epsilon = 0.0661 # j/mol
sigma = 0.3345 # nm

def lj_pot():
    '''
    calculates the Lennard-Jones potential based on pregiven parameters
    it only asks for the distance between the particles    
    '''
    r = input('Enter inter-atomic distance?',)
    r = float(r)
    V = round(4*epsilon*((sigma/r)**12-(sigma/r)**6),12)
    return 'V = ' + str(V)
    
#print(lj_pot())

def read_Natoms():
    '''
    asks the user for an int number of atoms
    '''
    n = input('Number of atoms?')
    n = int(n)
    return n
#print(read_Natoms())    

def read_atom_mass(n):
    '''
    reads the mass of n (int) atoms and returns a list of floats of them
    '''
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
    '''
    builds a distance matrix out of the coordianates list
    '''
    dis = []
    for i in range(len(coord)):
        dis1 = []
        for j in range(len(coord)):
            d = sqrt((coord[i][0]-coord[j][0])**2+(coord[i][1]-coord[j][1])**2+(coord[i][2]-coord[j][2])**2)
            dis1.append(d)
        dis.append(dis1)
    return dis

#print(get_distances([[3,3,3],[0,0,0],[0,0,0]]))

def V_lj(coord):
    '''
    takes a coordiantion list and calculates the Lennard-Jones potential
    '''
    V = 0
    distances = get_distances(coord)
    for i in range(0,len(distances)):
        for j in range(1, len(distances)):
           
    return V

    
def main():
    Natoms = read_Natoms()
    coord = read_atom_coord(Natoms)
    
    #distances = get_distances(coord)
    print(V_lj(coord))
#    for d in distances:
#        print(d)

main()