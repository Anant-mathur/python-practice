def add_10(x):
    return x+10

numbers = [1,2,3,4,5,6]

print(list(map(add_10,numbers))) # In Map, we have to pass a function as an argument(1st arg) and an iterable as the 2nd argument on which we want the mapping functiont to run on

# Adding two lists using map

numbers1 = [1,2,3,4,13]
numbers2 = [5,6,7,8,11]

print(list(map(lambda x,y:x+y, numbers1, numbers2)))

#Converting list of strings to integers
try:
    numbers = ['1', '2', '3', '4', '5','6']
    print(list(map(int,numbers)))
except ValueError:
    print("Invalid input")

#Getting name values from a dictionary
dict = [
        {"name":"Anant","age":22},
        {"name":"Roop","age":21},
        {"name":"Mathur","age":20}
    ]

def get_name(dict):
    return dict['name']

print(list(map(get_name,dict)))