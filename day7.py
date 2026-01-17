### Functions ###
# Creating a Function
def my_fun():
    print("This is my function")

# Calling a Function (even multiple times in a row)
my_fun()
my_fun()

# Example before and after function
temp1 = 77
celsius1 = (temp1 - 32) * 5 / 9
print(celsius1)

temp2 = 96
celsius1 = (temp2 - 32) * 5 / 9
print(celsius2)

temp3 = 50
celsius1 = (temp3 - 32) * 5 / 9
print(celsius3)

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5 / 9
print(fahrenheit_to_celsius(77))
print(fahrenheit_to_celsius(96))
print(fahrenheit_to_celsius(50))

# Returning Values
def get_greeting():
    return("Hello!")
message = get_greeting()
print(message)
#OR
print(get_greeting())

#even in this case, pass statement (+eventually specify todo action) for later use

# Function Arguments and Parameters
#Inside parentheses, separeted by comma
def my_function(fname): #fname is the parameter, the variable listed in the function definition
    print(fname + " La Porta")
my_function("Maria") #"Maria" is the argument
my_function("Raffaella") # actual value sent to the function
my_function("Patrizia") #when called

# Default Parameter Values
def my_function_2(name = "friend"):
    print("Hello", name + "!!!")
my_function_2("Paola")
my_function_2()

def dogs_function(animal, name):
    print("I have a", animal + ".")
    print("My", animal + "'s name is", name)
dogs_function(animal = "dog", name = "Charlie" + "!") #position doesn't matter
dogs_function("dog", "Buddy") #position matters

def dogs_function_p(animal, name, /): #positional-only arguments
    print("I have a", animal + ".")
    print("My", animal + "'s name is", name)

def dogs_function_k(*, animal, name): #keyword-only arguments
    print("I have a", animal + ".")
    print("My", animal = "dog" + "'s name is", name = "Charlie")

# Passing different data types
def fruit_function(fruits):
    for fruit in fruits:
        print(fruit)
my_fruits = ["banana", "pear", "apple"]
fruit_function(my_fruits)

def my_ffunction(person):
    print("Name:", person["name"])
my_person = {"name": "Paola", "surname": "La Porta"}
mu_ffunction(my_person)

# Returning Values
def my_new_function(x, y):
    return x + y
result = my_new_function(2, 5)
print(result)

# Returning different data types
def my_func():
    return ["apple", "banana"]
fruits = my_func()
print(fruits[0])

# *args and *kwargs
def my_function(*kids):
    print("Type:", type(kids))
    print("the youngest child is " + kids[2])
    print("All kids:", kids)
my_function("Emil", "Tobias", "Linus")

# *args and regular arguments
#Hello assigned to greetin, the rest to names
def my_function(greeting, *names):
    for name in names:
        print(greeting, name)
my_function("Hello", "John", "Paul", "Robert")

# Example: find the maximum value
def My_Function(*numbers):
    if len(numbers) == 0:
        return None
    max_num = numbers[0]
    for num in numbers:
        if num > max_num:
            max_num = num
    return max_num
print(my_function(3, 5, 9, 12, 13, 7, 2))

# **kwargs or keyword arguments
# if number of keyword arguments is not known
# **kwargs becomes a dictionary containing all the keyword arguments
def my_function(**kid):
    print("His last name is " + kid["lname"])
my_function(fname = "Tobias", lname = "White")

def my_function(**myvar):
    print("Type:", type(myvar))
    print("Name:", myvar["name"])
    print("Age:", myvar["age"])
    print("All data:", myvar)

my_function(name = "John", age = 30, city = "Dresden")

#Combining *args and **kwargs
def my_function(title, *args, **kwargs):
    print("Title:", title)
    print("Positional arguments:", args)
    print("Keyword arguments:", kwargs)
my_function("User Info", "Paul", "John", age = 25, city = "Paris")

# Unpacking using * and **
def my_function(a, b, c):
    return a + b + c
numbers = [1, 2, 3]
result = my_function(*numbers) #Same as my_function(1, 2, 3)
print(result)

def my_function(fname, lname):
    print("Hi", fname, lname)
person = {"fname": "Paul", "lname": "White"}
my_function(**person) #Same as (fname="Paul", lname="White")

# Global and Nonlocal variables
def function():
    global x #so that it belongs to the global scope
    x = 100
function()
print(x)

def function():
    x = 12
    def function1():
        nonlocal x #so that it belongs to the outer function
        x = 32
    function1()
    return x
print function()

#LEGB rule – Local, Enclosed, Global, Built-in
x = "global"
def outer():
  x = "enclosing"
  def inner():
    x = "local"
    print("Inner:", x)
  inner()
  print("Outer:", x)
outer()
print("Global:", x)