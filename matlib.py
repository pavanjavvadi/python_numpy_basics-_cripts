#numpy.matlib is used for matrices instead of numpy ndarray objects
#matrices functions

#importing the numpy module
import numpy as np 

#importing the numpy.matlib module
import numpy.matlib as nm

#matlib empty function
print("\nprinting the matrix with uninitializing the values using empty function:")
print(nm.empty((3,3)))

#matlib zeros function
print("\n\nprinting the matrix with initializing the values with value \"0\" using zero function:")
print(nm.zeros((3,3),dtype=int))

#matlib ones function
print("\n\nprinting the matrix with initializing the values with value \"1\" using ones function:")
print(nm.ones((3,4),dtype=int))

#matlib eye function
print("\n\nprinting the matrix with diagonal elements values equals to 1:")
print(nm.eye(n=4,k=0,dtype=int,M=5))

#matlib identity function
print("\n\nprinting the identity matrix is the one with diagonal elements initializes to 1 and all other elements to zero:")
print(nm.identity(5,dtype=int,))

#matlib random function
print("\n\nprinting the matrix with random values:")
print(nm.rand((5,5)))
