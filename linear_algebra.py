#linear algebra
#------------------------------------------------------------------

#importing the numpy module
import numpy as np  

#creating the array objects a and b
a = np.array([[1,2,3],[4,5,6],[7,8,9]])  
b = np.array([[23,23,12],[2,1,2],[7,8,9]])   

#dot product
dot = np.dot(a,b)  
print("\nprinting the output of dot product:\n",dot) 

#vdot
vdot = np.vdot(a,b)
print("\n\nprinting the output of vdot product:\n",vdot)

#inner
inner = np.inner(a,b)
print("\n\nprinting the output of inner function:\n",inner)

#matmul
matmul = np.matmul(a,b)
print("\n\nprinting the output of matrix multiplication:\n",matmul)

#linear algebric functions:
#----------------------------------------------
#det
det = np.linalg.det(a)
print("\n\nprinting the determinant of the array object \"a\":\n",det)

#solve function:
#This function is used to solve a quadratic equation where values can be given in the form of the matrix.
solve = np.linalg.solve(a,b)
print("\n\nprinting the output:\n",solve)

#inverse function:
inv = np.linalg.inv(a)
print("\n\nprinting the multiplicative inverse of the array object a:\n",inv)