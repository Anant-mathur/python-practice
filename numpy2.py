import numpy as np


x = np.array([1, 2, 3])

y = np.array([[1,2,3],[4,5,6]])
print(np.shape(x))
print(np.shape(y))

#Using arange
range_array = np.arange(1,10, dtype=np.int8)
print(range_array)
print(np.shape(range_array))

#Using linspace
linspace_array = np.linspace(0, 10, num=4)
print(linspace_array)
print(np.shape(linspace_array))

#Using linspace
logspace_array = np.logspace(0, 10, num=10)
print(logspace_array)
print(np.shape(logspace_array))

#Using zeros
zeros_array = np.zeros((3,4), dtype=np.int8)
print(zeros_array)
print(np.shape(zeros_array))

#Using ones
ones_array = np.ones((3,4), dtype=np.int8)
print(ones_array)
print(np.shape(ones_array))

#Using full
eights_array = np.full((3,4),fill_value=8, dtype=np.int8)
print(eights_array)
print(np.shape(eights_array))

#Using eye
i3_matrix = np.eye(3)
print(i3_matrix)
print(np.shape(i3_matrix))

#Using random
random_array = np.random.rand(3, 4)
print(random_array)
print(np.shape(random_array))

#Using random int
random_array2 = np.random.randint(1, 10000000, size=(3, 4))
print(random_array2)
print(np.shape(random_array2))

#Load csv
csv_data =np.loadtxt('file.csv', delimiter=',')
print(csv_data)
print(np.shape(csv_data))