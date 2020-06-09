#string functions with the array elements(string)

#importing the numpy module
import numpy as np 

#adding the two corresponding array elements
print("concatinating two array elements;")
print(np.char.add(["welcome","hi"],["pavan","P J"]))

#multiply the string with the number
print("\n\nmultiply the string element:")
print(np.char.multiply("hello pavan",2))

#center the array element
print("\n\ncenter the array element:")
print(np.char.center("python",20,fillchar="*"))

#capitalize the word
print("\n\ncapitalize the first letter of the word:")
print(np.char.capitalize("pavan"))

#title
print("\n\ncapitalize the every first letter of the word;")
print(np.char.title("welcome to the VS code"))

#lower
print("\n\nlower all the elements:")
print(np.char.lower("THIS IS PYTHON"))

#upper
print("\n\nupper all the elements:")
print(np.char.upper("this is visual studio code"))

#split
print("\n\nspliting the elements:")
print(np.char.split("this is python numpy library",sep=" "))

#splitlines
print("\n\nsplitlines:")
print(np.char.splitlines("hello\nworld!"))

#join
print("\n\nconcatination of all the strings specified in the sequence:")
print(np.char.join(":","HM"))

#replace
print("\n\noriginal string: w\"welcome pavan\"")
print("\nreplacing the word pavan with python:")
print("\nreplaced string")
print(np.char.replace("welcome pavan","pavan","python",count=0))

#encode and decode 
enstr = np.char.encode("welcome to javatpoint",'cp500',)  
dstr =np.char.decode(enstr, 'cp500')  
print(enstr)  
print(dstr) 