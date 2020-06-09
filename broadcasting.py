#broadcasting----
#we consider the matrix multiplication operation.
#If the shape of the two matrices is the same then this operation will be easily performed.
#However, we may also need to operate if the shape is not similar by using the broadcasting method

#importing the module
import numpy as np  

#creating the arrau with shape(3,4)
a = np.array([[1,2,3,4],[2,4,5,6],[10,20,39,3]])  
#creating the array with shape(4,)
b = np.array([2,4,6,8])  

print("\nprinting array a..")  
print(a)  
print("\nprinting array b..")  
print(b)  
print("\nAdding arrays a and b ..")  
c = a * b;  #the addition is made by repeating the elements of b as in the form [[2,4,6,8],[2,4,6,8],[2,4,6,8]] then add ition is performed
print(c)  
