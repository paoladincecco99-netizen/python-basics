### Decorators ###
#Take another function as input and returns a new function
#To add extra behaviour to a function w/o changing its code
#Example: a basic decorator that uppercases the return value of the decorated function
def changecase(func):
    def myinner():
        return func().upper()
    return myinner

@changecase #decorator
def myfunction(): #the function that gets decorated
    return "Hello"
print(myfunction())

@changecase
def otherfunction():
    return "I am happy!"
print(otherfunction())

#Arguments in the decorated function
def changecase(func):
    def myinner(x): #add the argument
        return func(x).upper() #add the argument
    return myinner

@changecase
def myfunction(nam):
    return "Hello " + nam
print(myfunction("Paola")) #pass the argument

# *args and **kwargs
def changecase(func):
    def myinner(*args, **kwargs):
        return func(*args, **kwargs).upper()
    return myinner

@changecase
def myfunction(surnam):
    return "Hello Mrs. " + surnam
print(myfunction("La Porta"))

# Own arguments
#Example: A decorator factory that takes an argument 
# and transforms the casing based on the argument value.
def changecase(n):
    def changecase(func):
        def myinner(): #...based on the argument value...
            if n == 1: 
                a = func().lower()
            else:
                a = func().upper()
            return a
        return myinner
    return changecase

@changecase(2)
def myfunction():
    return "Hellooo!"
print(myfunction())

# Multiple decorators
def changecase(func):
    def myinner():
        return func().upper()
    return myinner

def addgreeting(func):
    def myinner():
        return "Hello " + func() + ", have a good day!"
    return myinner

@changecase
@addgreeting
def myfunction():
    return "Paola"
print(myfunction())

# Preserving function Metadata
#Returning a function's name with __name__ attribute
def myfunction():
    return "Have a good day!"
print(myfunction.__name__)

#Import functools.wraps to preserve name and docstring when decorating
import functools
def changecase(func):
    @functools.wraps(func)
    def myinner():
        return func().upper()
    return myinner

@changecase
def myfunction():
    return "Goodbye!"
print(myfunction.__name__)


### Lambda ###
# It can take any number of arguments but only one expression
#Syntax
# lambda arguments : expression
x = lambda a : a + 10
print(x(9))

x = lambda a, b : a * b
print(x(3, 2))

x = lambda a, b, c : a + b + c
print(x(1, 2, 3))

# Useful when used in another functions
#Example: a function definition that takes one argument, 
# and that argument will be multiplied with an unknown number
def myfunc(n):
    return lambda a : a * n
mydoubler = myfunc(2)
print(mydoubler(11))
mytripler = myfunc(3)
print(mytripler(11))

#With Built-in functions+
#double all numbers in a list
numbers = [1, 2, 3]
doubled = list(map(lambda x: x * 2, numbers)) #map() applies a function to every item in an iterable
print(doubled)

#filter out even numbers from a list
numbers = [1, 2, 3, 4, 5, 6, 7, 8]
odd_numbers = list(filter(lambda x: x % 2 != 0, numbers))
print(odd_numbers)

#sort a list of tuples by the second element
students = [("John", 23), ("Paul", 22), ("Jack", 25)]
sorted_students = sorted(students, key=lambda x: x[1]) #in this case, based on age
print(sorted_students)

words = ["pineapple", "apple", "pine", "mug", "me"]
sorted_words = sorted(words, key=lambda x: len(x))
print(sorted_words)
