#importing the numpy module
import numpy as np


#creating an ndarray object
a = np.array


#passing  collection object in the array object
# b = np.array(object= list tuple str etc,dtype=type of data,copy= copy the object,order= roworder, columnorder,any,
# subok= make it as subclasses,ndmin = minimum dimensions)


c = np.array([1,2,3,4,5,6,7]) #creating an ndarray object

print("item size of the array element =",c.itemsize) #finding the item size
print("datatype of the object = ",c.dtype) #finding the datatype
print("shape of the array = ",c.shape) #finding the shape
print("size of the array = ",c.size) #finding the size

d = np.array([[1,2,3,4],[4,5,6,5],[7,8,9,1]])
print(f"printing the old array:\n{d}") #printing the old array element

e = d.reshape(4,3)
print(f"printing the reshaped array element:\n{e}") #printing the reshaped array

x=d[0,1]
print("slizing the array element = ",x) #printing the 1th index 2nd element i.e "6"


#linespace = the function only returns the evenly spaced values for the given interal

f = np.linspace(5,15,10)
print(f) #printing the linspacing values

print("maximum value in the C array object = ",c.max()) #maximum value in the array
print("minimum value in the C array object = ",c.min()) #minimum value in the array
print("sum of the array elements = ",c.sum()) # sum of the array elements 


#numpy array axis where (axis = 0 defines columns) and (axis = 1 defines rows)

print("maximum value in the D array columns object  = ",d.max(axis=0)) #finding max value in all columns of the object
print("minimum value in the D array  row object = ",d.min(axis=1)) #finding minimum value in all rows of the object
print("sum of the array elements = ",d.sum(axis=0),d.sum(axis=1))

#finding the square root and standard deviation of the array object

print("square root of the array object = ",np.sqrt(d)) #square root
print("standard deviation of the arrauy object = ",np.std(d))


#arthimectic operations can be also performed directly in numpy

g = np.array([[1,12,3,4],[14,15,16,1],[7,18,9,4]])
print("addition of the array objects = ",d+g)
print("substraction of the array objects = ", d-g)
print("multiplication of the array objects = ",d*g)


#array can be concatenated by vertical stack or horizontal stack

print("vertical stack = ",np.vstack((d,g))) #vertical stack
print("horizontal stack = ",np.hstack((d,g))) #horizontal stack