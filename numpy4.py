import numpy as np

arr = np.loadtxt('file.csv',delimiter=',')
print(arr)
print(arr.dtype)
print(arr.ndim)

#Indexing/Slicing of Data
print(arr[0])
print(arr[0,2])
print(arr[:4,:])#First 4 rows only
print(arr[:4])#First 4 rows only (Both ways work)
print(arr[:,:3])#First 3 cols only
print(arr[:2,:3])#First 3 cols only

# Filtering of Data 
# Need values>3
print((arr%2 == 0) | (arr<3)) #Gives boolean array whether condition is true or false
print(arr[(arr%2 == 0) | (arr<3)]) #Gives array
print(arr[(arr%2 == 0) & (arr<3)]) #Gives array

