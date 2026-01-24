# Testing packages
import math
import camelcase
c = camelcase.CamelCase()
txt = "hello world"
print(c.hump(txt))

import pyfiglet
x = pyfiglet.figlet_format("Python Rules!")
print(x)

import wikipedia
wikipedia.set_lang("en")
topic = "Circular Economy"
summary = wikipedia.summary(topic, sentences = 3)
print(f"Here's what I found on {topic}:", summary)

from colorama import Fore, Style
print(Fore.RED + "This message is red!")

### Try Except ###
try: #to test a block of code for errors
    print(x)
except: # to handle the error
    print("An exception occurred")

try:
    print(x)
except NameError:
    print("Variable x is not defined")
except:
    print("Something else went wrong")
else: #to execute the code when there is no error
    print("Nothing went wrong")
finally: #to execute regardless the result 
    print("The try except is finished")

#Trying opening and writing a file that is not writable
try: 
    f = open("demofile.txt")
    try:
        f.write("Lorem Ipsum")
    except:
        print("Something went wrong writing to the file")
    finally:
        f.close()
except:
    print("Something went wrong opening the file")

# Raising an exception
x = -1
if x < 0:
    raise Exception("Sorry, no negative numbers :(")

#To define what kind of error to raise:
x = "Hi"
if not type(x) is int:
    raise TypeError("Only integers are allowed here!")

### Strings Formatting ###
# F-Strings
txt = f"The price is 20 dollars" #to format selected parts of a string
print(txt)

# Placeholders and Modifiers
price = 20
txt = f"The price is {price} dollars" #can contain variables, operations, functions...
print(txt)
txt1 = f"The price is {price:.2f} dollars" #modifier to display price with 2 decimals
print(txt1)
txt2 = f"The price is {99:.2f} dollars"
print(txt2)

# Operations in F-Strings
txt = f"The price is {20 * 2} dollars"
print(txt)

price = 59
tax = 0.25
txt = f"The price is {price + (price * tax)} dollars"
print(txt)
#If... else inside placeholders
txt1 = f"It is very {'Expensive' if price>50 else 'Cheap'}"
print(txt1)

#Executing functions
fruit = "apples"
txt = f"I love {fruit.upper()}"
print(txt)

#Creating a function
def myconverter(x):
    return x * 0.3048
txt = f"The plane is flying at a {myconverter(30000)} meter altitude"
print(txt)

#Comma separator
price = 3000
txt = f"The price is {price:,} dollars"
print(txt)

### None ###
x = None 
print(x)
print(type(x))
 
# Comparing to None
result = None
if result is None:
    print("No result")
else:
    ("Result is ready")
#OR
if result is not None:
    print("Result is ready")
else:
    print("No result yet")

# None as a False
print(bool(None))

# Functions returning None
def myfunc(): #because it doesn't have a return statement
    x = 5
x = myfunc()
print(x)

### User Input ###
print("Enter your name:")
name = input()
print(f"Hello {name}")

name = input("Enter you name:")
print(f"Hello {name}")

# Multiple inputs
name = input("Enter your name:")
print(f"Hello {name}")
fav1 = input("What is your favorite animal:")
fav2 = input("What is your favorite color:")
print(f"Do you want a {fav2} {fav1}?")

# Input Number 
x = input("Enter a number:")
y = math.sqrt(float(x))
print(f"The square root of {x} is {y}")

# Validate input
y = True
while y == True: #keeps asking until it gets a number
    x = input("Enter a number:")
    try:
        x = float(x);
        y = False
    except:
        print("Wrong input, please try again.")
print("Thank you!")



