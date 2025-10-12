#Array Operations using numpy
import numpy as np

#Arithmetic Operations
data = np.arange(1,10)
data2 = data+1
data3 = data-1
data4 = data*3
data5 = data/2
data6 = data//2

print(data)
print(data2)
print(data3)
print(data4)
print(data5)
print(data6)

#Linear Algebra
A = np.array([[1,2,3],[4,5,6],[7,8,9]])
B = np.array([[9,8,7],[6,5,4],[3,2,1]])

C = np.matmul(A,B)  #Matrix Multiplication

print(C)

#Get the determinant of a square matrix
matrix = np.array([[1,12,3],[4,5,61],[7,18,9]])
det = np.linalg.det(matrix)
print(det)

#Statistics
data = np.array([[1,2,3,4,5,6,7,8,9,10],[5,6,7,8,9,10,11,12,13,14]])
print("Mean is:",np.mean(data))
print("Median is:",np.median(data))
print("Standard Deviation is:",np.std(data))
print("Variance is:",np.var(data))
print("Max is:",np.max(data))
print("Min is:",np.min(data))
print("Max is:",np.max(data,axis=1))#Along 1 axis
print("Min is:",np.min(data,axis=1))#Along 1 axis
