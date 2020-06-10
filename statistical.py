#statistical functions
#----------------------------------------------------

#importing the numpy module
import numpy as np 

#statistical functions:

#creating the a array object
a = np.array([[1,2,3],[4,5,6],[7,8,9]])
#creating the b array object
b = np.array([[9,8,7],[6,5,4],[3,2,1]])

#finding the maximum item value among the rows and columns
print("\n\nprinting the maximum values from \"a\" using the row axis:",np.amax(a,axis=1))
print("printing the maximum values from \"b\" using column axis:",np.amax(b,axis=0))

#finding the minimum item values among the columns and rows
print("\n\nprinting the minimum values from a using the column axis;",np.amin(a,axis=0))
print("printing the minimum values from\"b\" using the row axis:",np.amin(b,axis=1))

#peak to peak--it gives a range of values along the axis
print("\n\nprinting the range of values from \"a\" using the row axis",np.ptp(a,axis=1))
print("printing the range of values from  \"b\" using the column axis",np.ptp(b,axis=0))

#percentile function
print("\n\nprinting the percentage of the array \"a\"",np.percentile(a,q=100,axis=1))
print("printing the percentage values of the array element b:",np.percentile(b,q=50,axis=0))

#median function
print("Median of array along axis 0:")
print(np.median(a,0))  

#mean function
print("Mean of array along axis 0:",np.mean(a,0)) 

#average function
print("\n\nprinting the average value of the row axis and column axis of a and b respectively:")
print(np.average(a,axis=1))
print(np.average(b,axis=0))