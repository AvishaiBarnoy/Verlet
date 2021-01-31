#!/home/avishaib/miniconda3/bin/python

import math
import numpy as np
import itertools as it
from scipy.spatial import distance_matrix

def read_Natoms(file_path):
	with open(file_path) as f:
		return int(f.readline())

def read_atom_mass(file_path):
	return np.loadtxt(file_path,skiprows=2,usecols=0)

def read_atom_coord(file_path):
	return np.loadtxt(file_path,skiprows=2,usecols=(1,2,3))

def distances(coords):
	return distance_matrix(coords,coords)
	
def v_lj_sys(dist,n_atoms):
	e = 0.0661
	s = 0.3345
	v = 0
	for i in range(n_atoms):
		for j in range(i+1,n_atoms):
			v += 4*e*(math.pow(s/dist[i,j],12) - math.pow(s/dist[i,j],6))
	return v

def set_velocity(n_atoms):
	vel = [0.1, 0.2, 0.3]
	return np.array([ vel for i in range(n_atoms) ])

def e_tot(coord,mass,velocity,n_atoms):
	v_lj = v_lj_sys(distances(coord),n_atoms)
	T = 0
	v = np.sum(np.power(velocity,2),axis=1) # computes the size of the velocity vector
	for i in range(n_atoms):
		T += mass[i]*v[i]
	return v_lj + .5*T

def get_acceleration(coord,mass,h=1e-5):
#	a = np.zeros(coord.shape)
	e = 0.0661
	s = 0.3345
	a = []
	print(mass)
	print(coord)
	v = lambda pos: 4*e*(np.power(s/pos,12) - np.power(s/pos,6))
#	v += 			4*e*(math.pow(s/dist[i,j],12) - math.pow(s/dist[i,j],6))
	for i,j in enumerate(coord):
		print((-1/mass[i])*(v(j+h)-v(j-h))/(2*h))
#	for i,atom in enumerate(coord):
			
#	return np.array(a)

if __name__=='__main__':
	path = './inp2.xyz' 
	n_atoms = read_Natoms(path)
	mass = read_atom_mass(path)
	coords = read_atom_coord(path)
	dist_mat = distances(coords)
	v_lj = v_lj_sys(dist_mat,n_atoms)
	e_total = e_tot(coords,mass, set_velocity(n_atoms),n_atoms)
	acceleration = get_acceleration(coords,mass)
	print(acceleration)
#	print(N_atoms)
#	print(mass)
#	print(coords)
#	print(distances(coords))
#	print(v_lj)
#	print(e_total)
