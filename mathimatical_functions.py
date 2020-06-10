#numpy mathematical functions
#-------------------------------------------------------------------

#iporting the random module
import numpy as np 

#crerating the array object
a = np.array([1,2,3,4,5,6])

#trignometric functions
#_______________________________________________________________________
#sin
sin_ = np.sin(a*(np.pi/180))
print("printing the sin values of the array element:")
print(sin_)

#cos
cos_ = np.cos(a*(np.pi/180))
print("\n\nprinting the cos values of the array element:")
print(cos_)

#tan
tan_ = np.tan(a*(np.pi/180))
print("\n\nprinting the tan values of the array elements:")
print(tan_)

#cosec
cosec_ = np.arcsin(sin_)
print("\n\nprinting the cosec values of the array element:")
print(cosec_)
print("printing the cosec values in terms of degrees:")
print(np.degrees(cosec_))

#sec
sec_ = np.arccos(cos_)
print("\n\nprinting the sec values of the array element:")
print(sec_)
print("printing the sec values in terms of degrees:")
print(np.degrees(sec_))

#cot
cot_ = np.arctan(tan_)
print("\n\nprinting the cot values of the array element:")
print(cot_)
print("printing the cot values in terms of degrees:")
print(np.degrees(cot_))

#rounding function
round_ = np.round(sin_,decimals=2)
print("\n\nprinting the sin values with 2 decimal points using round function:")
print(round_)
print("printing the same sin values with -1 decimal points using round function:")
print(np.round(sin_,decimals=-1))

#floor function
floor_ = np.floor(cos_)
print("\n\nprinting the cos values using floor fnction:")
print(floor_)

#ceil function
ceil_ = np.ceil(tan_)
print("\n\nprinting the tan values using ceil function:")
print(ceil_)