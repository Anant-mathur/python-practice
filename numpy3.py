#Array Attributes
import numpy as np

x = np.array([[1,2,3],[4,5,6]])
print("Shape is:",x.shape)
print("Number of dimensions is:",x.ndim)
print("Size of each element is:",x.itemsize)
print("Total number of elements is:",x.size)
print("Total number of bytes is:",x.nbytes)
print("The datatype is:",x.dtype)

#Array Operations
print("The transpose is:\n",x.transpose())  #Transpose the matrix
print("The transpose is:\n",x.T)  #Transpose the matrix

print("Reshaped array is :\n",x.reshape(3,2))  #Reshape the matrix doesn't change original matrix,x.resize(2,3)  #Resize the matrix changes original matrix

x.resize(2,3)  #Resize the matrix changes original matrix
print("The original array is:\n",x)

print("The flattened array is:",x.flatten()) #Converts n-d array to 1-d array

#Stacking arrays
a = np.array([[1,2],[3,4]])
b = np.array([[5,6],[7,8]])
print("Vertical Stack:\n",np.vstack((a,b)))  #Vertical Stack
print("Horizontal Stack:\n",np.hstack((a,b)))  #Horizontal Stack
