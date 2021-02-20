# Verlet Algorithm
This is a simple program calculating the Verlet algorithm for molecular dynamics (MD) taking into account only kinetic energy and the Lennard-Jones (LJ) potential. Therefore it is most suitable for noble gas simulations, like Argon which is in the example. Inert gasses (e.g., N<sub>2 </sub>) can also be simulated using this approximation but covalent bonds are not yet implemented.

The LJ potential is defined for same-species atoms/molecules therefore mixed systems are not supported.

## Dependancy list
Stadard libraries that this repository depend on:
1. numpy
2. scipy 

# Updates 

## 20.02.21:
1. Verlet algorithm now produces output file according to tutorial file
2. Added parameters file, currently only for masses

## 19.02.21:
1. changed angstrom to nm
2. fixed get_acceleration
3. finished verlet algorithm
4. formatting now produces .xyz files readable by VMD
5. minor function changes (like get velocity)
6. mass is now read from dictionary and not from input file
 
# To Do:
2. Add parameters dictionaries: masses using #n and name, LJ
3. Change verlet function to output steps into memeory and then save as file instead of std

# Future projects:
1. Add Columb interactions
2. Check TMPChem youtube tutorials
3. Random seed for veloctiy distribution, temperature based
4. Random positioning
5. Parallelization
6. PBC
7. Covalent bond option
