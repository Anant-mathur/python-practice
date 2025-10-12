#To zip arrays together

arr1 = [1,2,3,4,5]
arr2 = [6,7,8,9,10]

zipped_array = zip(arr1,arr2)
print(list(zipped_array))

#If arrays aare of unequal length, it stops at the shortest one
arr1 = [1,2,3,4,5]
arr2 = [6,7,8,9,10,11]

zipped_array = zip(arr1,arr2)
print(list(zipped_array))

#Unzip
arr1,arr2 = zip(*zip(arr1,arr2))
print(list(arr1))
print(list(arr2))