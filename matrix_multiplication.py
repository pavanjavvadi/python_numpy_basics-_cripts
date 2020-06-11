#matrix multiplication
#-------------------------------------------------------
#three methods of matrix multiplication
#multiply function
#dot function
#matmul function


#mporting the module
import numpy as np 

#creating the array object
a = np.array([[1,2,3],[4,5,6],[7,8,9]],ndmin=3)  
b = np.array([[9,8,7],[6,5,4],[3,2,1]],ndmin=3)  
result = np.multiply(a,b)  
print("\nprinting the matrix after multipication using multiply function:\n")
print(result)

result1 = np.dot(a,b)
print("\n\nprinting the matrix using dot product:\n")
print(result1)

result2 = np.matmul(a,b)
print("\n\nprinting the matrix using matmul function:\n")
print(result2)