#iterations can also be performed on the array i.e nditer is used to iterate over the given array using python standard iterator interface

#importing the module
import numpy as np 

#creating the array object
a = np.array([[1,12,3,4],[14,15,16,1],[7,18,9,4]])

print("original array:")
print(a)

#iterating with for loop
for x in np.nditer(a):
    print(x,end=" ")

#creating the transpose matrix
transpose_ = a.T
print("\ntranspose array:")
print(transpose_)

#iterating the transpose using for loop
for y in np.nditer(transpose_):
    print(y,end=" ")

#copying the array element items
b = a.copy(order="c")
print("printing the copied array elements")
print(b)

#array values modification
for z in np.nditer(a):
    z = z * 3
    print(z,end=" ")