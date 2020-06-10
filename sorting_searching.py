#sorting and searching 
#------------------------------------------
#sorting and searching are also performed on the array elements using numpy

import numpy as np 
a = np.array([[1,23,31,14],[49,15,6,55],[79,81,39,10]])
ba =  np.array([18,13,60,23,54,9])


#sorting--quicksort default
b = np.sort(a,axis=0)
print("\nprinting the array  column elements using the quicksort:")
print(b)
print("\nprinting the array row elements using the quicksort")
print(np.sort(a,axis=1))
#creating the datatype
data_type = np.dtype([("name","S10"),("marks",int)])
#creating the array
arr = np.array([("pavan",200),("aadhya",251)],dtype=data_type)
print("\nsorting array by name:")
print(np.sort(arr,order="name"))
print("\nsorting array by marks:")
print(np.sort(arr,order="marks"))

#sorting--argsort == it returns the index of the array which is used to construct the array
print("\n\n\nprinting the array  row elements indexes using the argsort:")
c =np.argsort(ba)
print(c)
print("\nprinting the elements of array:")
for j in c:
    print(ba[j],end=" ")

#sorting--lexsort == sort the array using the sequence of keys indirectly
#creating e annd f array objects:
e = np.array(['a','b','c','d','e'])  
f = np.array([12, 90, 380, 12, 211])  

#creating the array using lexsort 
indexes = np.lexsort((e,f))  
  
print("\n\n\nprinting indices of sorted data")  
print(indexes)  
print("\nusing the indices to sort the array")  
  
for i in indexes:  
    print(e[i],f[i])

#non-zero functions
print("\n\nprinting the nonzero index positions:")
print(np.nonzero(f))

#where function
print("\n\nprinting the array element indexes using where function:")
print(np.where(f>100))
