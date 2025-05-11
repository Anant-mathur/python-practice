# Filter function
def is_even(num):
    return num % 2 == 0

numbers = [1,2,3,4,5,6,7,8,9,10]
list(filter(is_even,numbers))

#Filter the list and only get numbers that are greater than 5
my_numbers = [3,2,11,33,1,-1,22,9,22]

list(filter(lambda x:x>5,my_numbers))

#Filter the list and only get numbers that are greater than 5 snd lesser than 15
my_numbers = [3,2,11,33,1,-1,22,9,22]

list(filter(lambda x:x>5 and x<15,my_numbers))

#Check if age is greater than 20 in a dictionary and filter them out

dict = [
        {"name":"Anant","age":22},
        {"name":"Roop","age":21},
        {"name":"Mathur","age":20}
    ]


print(list(filter(lambda x : x['age']>21,dict)))
