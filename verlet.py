#!/home/avishaib/miniconda3/bin/python

import math
import numpy as np
import itertools as it
from scipy.spatial import distance_matrix

mass_dict = {'Ar':39.948,18:39.948}

def read_Natoms(file_path):
	with open(file_path) as f:
		return int(f.readline())

def get_atom_mass(file_path):
	index = np.loadtxt(file_path,skiprows=2,usecols=0)
	mass = []
	for i in index:
		mass.append(mass_dict[i])
	return np.array(mass)

def read_atom_coord(file_path):
	return np.loadtxt(file_path,skiprows=2,usecols=(1,2,3))

def distances(coords):
	return distance_matrix(coords,coords)
	
def v_lj_sys(dist,n_atoms):
	e = 0.0661
	s = 0.3345 # angstrom
	s = 3.345 # nm
	v = 0
	for i in range(0,n_atoms):
		for j in range(i+1,n_atoms):
			v += 4*e*(math.pow(s/dist[i,j],12) - math.pow(s/dist[i,j],6))
	return v

def set_velocity(n_atoms):
	'''
	depracted
	now using manual velocity input into the verlet function
	'''
	vel = [0.1, 0.2, 0.3]
	return np.array([ vel for i in range(n_atoms) ])

def e_tot(coord,mass,velocity,n_atoms):
	v_lj = v_lj_sys(distances(coord),n_atoms)
	T = 0
	v = np.sum(np.power(velocity,2),axis=1) # computes the size of the velocity vector
	for i in range(n_atoms):
		T += mass[i]*v[i]
	return v_lj + .5*T

def get_acceleration(coord,mass):
	'''
	This function computes the acceleration of each particle
	In the tutorial they asked to compute the derivative approximately,
	I was not successful in doing so, hence I computed using the exact derivative
	'''
	np.set_printoptions(suppress=True)
	e = 0.0661
	s = 0.3345 # angstrom
	s = 3.345  # nm
	a = np.zeros(coord.shape)
	dist_mat = distances(coord)
	for i in range(len(coord)):
		for j in range(i+1,len(coord)):
			temp_x = 24*e*(coord[i][0] - coord[j][0])*(s**6/dist_mat[i,j]**8 - 2*s**12/dist_mat[i,j]**14)
			temp_y = 24*e*(coord[i][1] - coord[j][1])*(s**6/dist_mat[i,j]**8 - 2*s**12/dist_mat[i,j]**14)
			temp_z = 24*e*(coord[i][2] - coord[j][2])*(s**6/dist_mat[i,j]**8 - 2*s**12/dist_mat[i,j]**14)
			a[i] += [-temp_x/mass[i],-temp_y/mass[i],-temp_z/mass[i]]
			a[j] += [temp_x/mass[j],temp_y/mass[j],temp_z/mass[j]]
	return a

def verlet(coord, mass, velocity,N_steps=1000,Delta_t=.1):
	'''
	computes the velocity verlet algorithm for Ar
	
	'''
	np.set_printoptions(suppress=True)
	energy = []
	n_atoms = read_Natoms(path)
	for step in range(N_steps):
		e_step = e_tot(coord,mass,velocity,n_atoms=len(mass))
		energy.append(e_step)
		acceleration_n = get_acceleration(coord,mass)
		print(n_atoms)
		print("Step:",step,"\t","E = ",e_step)
		for i in range(n_atoms):
#			print("Ar\t",round(coord[i][0],6),'\t',round(coord[i][1],6),'\t',round(coord[i][2],6))
			print(18,round(coord[i][0],6),round(coord[i][1],6),round(coord[i][2],6))
			coord[i] += velocity[i]*Delta_t + 0.5*acceleration_n[i]*Delta_t**2
		acceleration_n1 = get_acceleration(coord,mass)
		for i in range(n_atoms):
			velocity[i] += 0.5*(acceleration_n[i]+acceleration_n1[i])*Delta_t
	return coord, velocity, energy

if __name__=='__main__':
	path = './input_files/inp3.xyz' 
	n_atoms = read_Natoms(path)
	mass = get_atom_mass(path)
	coords = read_atom_coord(path)
	velocity = np.array([[0.,0.,0.] for i in range(n_atoms)])
	coord, velocity, energy = verlet(coords,mass,velocity,N_steps=1000,Delta_t=.1)
	with open('final_coords.rst','w') as f:
		f.write(str(n_atoms)+'\n')
		f.write('Position\n')
		f.writelines(np.array_str(coord)+'\n')
		f.write('velocity\n')
		f.writelines(np.array_str(velocity)+'\n')
		
