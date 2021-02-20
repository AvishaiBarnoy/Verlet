#!/home/avishaib/miniconda3/bin/python

import numpy as np
from scipy.spatial import distance_matrix

def GetGMagVdwIJ(r_ij, eps_ij, ro_ij):
	"""Calculate energy gradient magnitude of van der waals pair energy.
  	
	Args:
	r_ij (float): Distance [Angstrom] between atoms i and j.
	eps_ij (float): Van der Waals epsilon [kcal/mol] between pair ij.
	ro_ij (float): Van der Waals radius [Angstrom] between pair ij.
  
	Returns:
	g_vdw_ij (float): Magnitude of energy gradient [kcal/(mol*A)].
	"""
	rrel_ij = ro_ij / r_ij
	return -24.0 * (eps_ij / ro_ij) * (2*rrel_ij**13 - rrel_ij**7)
	#return -12.0 * (eps_ij / ro_ij) * (rrel_ij**13 - rrel_ij**7) # original

coords = np.array([[0,0,0],[0,0,.3],[.1,.2,-.3]])
dist_mat = distance_matrix(coords,coords)

#print(coords)
#print(dist_mat)
e = 0.0661 # j/mol
s = 0.3345 # Angstrom
mass = [10,20,15]
print(GetGMagVdwIJ(dist_mat[0,1],e,s)/mass[0],GetGMagVdwIJ(dist_mat[0,2],e,s)/mass[0])

#print(GetGMagVdwIJ(dist_mat[1,0],e,s)/mass[1],GetGMagVdwIJ(dist_mat[1,2],e,s)/mass[1])
#print(GetGMagVdwIJ(dist_mat[2,0],e,s)/mass[2],GetGMagVdwIJ(dist_mat[2,1],e,s)/mass[2])
#print(GetGMagVdwIJ(dist_mat[0,1],e,s)/mass[0])

