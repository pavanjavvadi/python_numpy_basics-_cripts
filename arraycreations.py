# we can construct the ARRAY OBJECTS by using different methods
#general syntax = numpy.type_of_method(shape=(row,column),order= default---c(row major order)&f-fortron (column major order),
#dtype=default(float))

#importing the module
import numpy as np 

#numpy empty
a = np.empty((3,3),dtype=int,order="c")
print("this is numpy empty for creating the array object with it own elements of defined shape and datatype:\n",a)

#numpy zeros
b = np.zeros((4,4),dtype=int,order="c")
print("This is numpy zeros array with all items intialized with value of 0 in defined shape:\n",b)

#numpy ones
c = np.ones((3,3),dtype=int,order="f")
print("This is numpy ones array with all items in the element initialized with value of 1 in defined shape and datatype:\n",c)