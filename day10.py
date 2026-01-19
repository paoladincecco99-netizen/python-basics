### Range ###
#Commonly used for looping a specific number of times,
# returns an immutable sequence of numbers
#syntax: range(start, stop, step)
x = range(10) #to create a range of numbers from 0 (default) to 9
x = range(3, 10) #range from 3 to 9
x = range(3, 10, 2) #from 3 to 9, with a step of 2
for i in range(10):
    print(i)

# Converting ranges to lists
print(list(range(6)))
print(list(range(1, 7)))
print(list(range(1, 11, 2)))

# Slicing ranges
r = range(11)
print(r[2])
print(r[:5])

# Membership testing
r = range(0, 11, 2)
print(6 in r) #to test if 6 is in the range
print(7 in r) #Returns False

# Length
r = range(0, 10, 2)
print(len(r))

### Arrays – or using lists as arrays ###
cars = ["Volvo", "Ford", "Fiat"]
x = cars[0] #to get the value of the first array item
cars[1] = "Toyota" #to modify the value of the first array item
x = len(cars)
for x in cars: #looping the array elements
    print(x)
cars.append("Honda") #adding one more element to the cars array
cars.pop(3) #to remove an element from the array
cars.remove("Volvo")

### Iterators ###
mytuple = ("apple", "banana", "pineapple")
myit = iter(mytuple)
print(next(myit))
print(next(myit))
print(next(myit))

mystr = "banana"
myit = iter(mystr)
print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))

# Creating an iterator
class MyNumbers:
    def __iter__(self):
        self.a = 1
        return self #returns numbers starting with one...
    def __next__(self):
        x = self.a
        self.a += 1 
        return x #and each sequence will increase by one
myclass = MyNumbers()
myiter = iter(myclass)

print(next(myiter))
print(next(myiter))
print(next(myiter))

#StopIteration
class MyNumbers:
    def __iter__(self):
        self.a = 1
        return self 
    def __next__(self):
        if self.a <= 20:
            x = self.a
            self.a += 1 
            return x
        else:
            raise StopIteration #to stop it at 20
myclass = MyNumbers()
myiter = iter(myclass)
for x in myiter:
    print(x)

### Modules ###
# Creating a Module to be saved in .py file
def greeting(name):
    print("Hello, " + name)

# Using a module
import mymodule
mymodule.greeting("Paola")
a = mymodule.person1["age"]
print(a)

# Renaming a module
import mymodule as mx
a = mx.person1["age"]
print(a)

# Built-in models and functions
import platform
x = dir(platform)
print(x)

#Import parts from module
from mymodule import person1
print (person1["age"])


### Datetime ###
#To work with dates as date objects
import datetime
x = datetime.datetime.now()
print(x)
print(x.year)
print(x.strftime("%A")) #this method takes the format parameter to specify

# Creating date objects
import datetime
y = datetime.datetime(2002, 5, 6)
print(y)


### Math ###
x = min(5, 10, 15)
y = max(3, 6, 2)
z = abs(-3.22) #absolute value of -3.22
w = pow(4, 3) #4 to the power of 3
import math #math module, built-in
x = math.sqrt(64) #square root of 64
y = math.ceil(1.4) #to round the number upwards
z = math.floor(1.4) #to round the number downwards
w = math.pi # pi greek value
