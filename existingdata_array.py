#python provides as the way to create the array from the existing data



#numpy asarray
#________________________________
#it is used to create an array by using the existing list or tuples which are created in python

#importing the module
import numpy as np 

#creating the list in python list form
list_items = [[1,2,3,4,5,6],[5,6,7,8,9],[1,8,5,3]]
print("\n\ndata type of list_items is :",type(list_items))
#numpy asarray using list
a = np.asarray(list_items,dtype=list,order="c") #printing the python list into array by using asarray function
print("datatype(dtype) of the array object is:",type(a))


#creating a tuple in python
tuple_items = ((1,2,3,4,5),(2,3,4,5))
print("\n\ndata type of the tuple_items is :",type(tuple_items))
#numpy assarray  using tuple
b = np.asarray(tuple_items,order="f") #printing the python tuple into array by using asarray function
print("datatype(dtype) of the array object is: ",type(b))



#numpy frombuffer
#__________________________________________
#this function is used to create the array by using the specified buffer

buffer_str = b'hello world!'
c = np.frombuffer(buffer_str,dtype='S2') # here s2 refers the length of the element similarly s1,s2,s3............refers length of the element
print("\n\ntype of buffer_str is :",type(buffer_str))
print ("type of c is:",type(c))


#numpy fromiter
#__________________________________________
#this function is used to create the array by using the iterating objects

iterator = iter(list_items)
d = np.fromiter(iterator,count=0,dtype=int)
print("\n\ntype of d is:",type(d))
print("type of list_items:",type(list_items))


##################################################################################################################################