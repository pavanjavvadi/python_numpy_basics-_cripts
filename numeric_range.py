#numpy array within the numeric range:
#------------------------------------------------------------------------
#arrays can be created by using the specified range.

#importing the random module
import numpy as np 

#numpy arrange
#------------------------------------------------------------------------
#syntax : numpy.arrange(start,stop,step,dtype)

a = np.arange(5,20,5,dtype=int)
print("numpy arrange values are:")
print(a)


#numpy linspace
#------------------------------------------------------------------------
#syntax : numpy.linspace(start,stop,num=even spaced values,endpoint = true or false,rettstep,dtype)

b = np.linspace(5,20,num=5,endpoint=True,dtype=float)
print("numpy linspace values are:")
print(b)


#numpy logspace -- it creates an array that are evenly spaced on a log scale
#-------------------------------------------------------------------------
#syntax : numpy.linspace(start,stop,num,endpoint,base,dtype)

c = np.logspace(3,10,num=20,endpoint=True,dtype=int,base=2)
print("numpy logspace values are:")
print(c)

##################################################################################################