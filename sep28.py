from numpy.ma.core import true_divide


def greet_user(name):
    print("Hello,",name,": Welcome to Python")

greet_user("carl")

def add_numbers(a,b):
    total = a + b
    return total

result = add_numbers(10,5)
print("10 + 5 =",result)

def describe_pet(name, animal="dog"):
    print(name,"has a",animal+".")

describe_pet("Milo")

def area_of_rectangle(width,height):
    area = width * height
    return area

room_area = area_of_rectangle(8,5)
print("the room is",room_area,"square feet")


def square(number):
    return number*number

def print_square_and_double(number):
    squared=square(number)
    doubled=number*2
    print("number:",number)
    print("doubled:",doubled)
    print("squared:",squared)

print_square_and_double(4)


def is_even(number):
    if number%2==0:
        return True
    return False

for value in [2,7,10,13,22]:
    print(value,"is even?",is_even(value))