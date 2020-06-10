#copy and views
#-------------------------------------

#importing the random module
import numpy as np  
#creating the array object
a = np.array([[1,2,3,4],[9,0,2,3],[1,2,3,19]])  
  
print("Original Array:\n",a)  
print("\nID of array a:",id(a))  
#copy the array object  
b = a   
  
print("\n\nmaking copy of the array a")  
print("\nID of b:",id(b))  
  
b.shape = 4,3;  
  
print("\nChanges on b also reflect to a:")  
print(a)  

#view method -- same original array but changes applied in copied array do not reflect the original array
c = np.array([[14,82,33,54],[92,40,42,63],[31,24,32,19]])  
  
print("Original Array:\n",c)  
print("\nID of array c:",id(a))  
#creating the new array b using view method 
d = c.view()  
  
print("\nID of d:",id(d))  
print("\nprinting the view d")  
print(d)  
  
d.shape = 4,3;  
  
print("\nChanges made to the view d do not reflect c")  
print("\nOriginal array \n",c)  
print("\nview\n",d) 

#copy method -- doesn't share the memory location with the original array
e = a.copy()  
print("\nID of e:",id(e))