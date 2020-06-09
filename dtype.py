import numpy as np # importing the numpy module

d = np.dtype(np.int32) #declaring the type of dtype where syntax = numpy.dtype(object=str,list,etc,align= (TorF)for adding extra padding,copy)
a = np.array([[1,2],[3.98,4.098]],dtype = d)
print(a)

# structured data type with the help of mapping(dict)
b = np.dtype([('sample',np.float64),('sample_int',np.int32)]) #declare sample with float dtype and sample_int with int dtype
c = np.array([[1,2],[3.98,4.098]],dtype = b) #ceating the array element
print(c['sample'])  #printing array elements in float dtype
print(c['sample_int']) #printing array elements in int dtype