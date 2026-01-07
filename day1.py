print("Hello, World!\nThis is my first Python script.")

# Check Python version
import sys
print(sys.version)

### Python syntax ###

# Indentation with basic arithmetic operations
if 5 > 2:
    print("Five is greater than two!")
    print("Performing some arithmetic operations between the two numbers:")
    sum_result = 5 + 3
    product_result = 5 * 3
    print(f"Sum: {sum_result}")
    print(f"Product: {product_result}")

# Python variables (created when value is assigned) )
x = 10          # Integer
y = 3.14        # Float
name = "Alice"  # String
is_student = True  # Boolean
print(f"Integer: {x}, Float: {y}, String: {name}, Boolean: {is_student}")

# Casting (to specify data type)
x = str(10)      # x will be '10' (string)
y = int(3.99)    # y will be 3 (integer)
z = float("5.67") # z will be 5.67 (float)
print(f"Casted values - x: {x} (type: {type(x)}), y: {y} (type: {type(y)}), z: {z} (type: {type(z)})")

# Semicolons to separate statements on the same line
a = 5; b = 10; print(f"a: {a}, b: {b}")

# Many values to multiple variables
p, q, r = 1, 2.5, "Hello"
print(f"p: {p}, q: {q}, r: {r}")
print(p)

# One value to multiple variables
m = n = o = 20
print(f"m: {m}, n: {n}, o: {o}")
print("m = n = o =", m)

# Global vs. local variables
global_var = "World"
def myfunc():
    print("Hello " + global_var)  # Accessing global variable
myfunc()

x = "awesome"
def myfunc2():
    x = "fantastic"  # Local variable
    print("Python is " + x)
myfunc2()
print("Python is " + x)  # Accessing global variable

def myfunc3():
    global x # Declaring x as global
    x = "superb"  # Modifying global variable (previously defined as "awesome")
myfunc3()
print("Python is " + x)


### Python output/print ###

print("Hello, World!", end=" ")  # end parameter to avoid newline
print(" - I will print on the same line.")

# No double quotes for numbers, math operations
print(42)
print(3.14159)
print(7 + 5)
print(10 / 2)

x = 5
y = 2
z = "apples"
print(x - y)
print(x, z)
print(x - y, z)

# Unpacking a list/tuple in print
fruits = ["Apple", "Banana", "Cherry"]
x, y, z = fruits
print(x, y, z)

days = ("Monday", "Tuesday", "Wednesday")
a, b, c = days
print( a, b, c)
print("The first 3 days of the week are:", a, b, c)

### Built-in Data types ###
x = 5
print(x, "belongs to", type(x))
y = ("apple", "banana", "cherry") # tuple, immutable
z = ["apple", "banana", "cherry"] # list, mutable
print(z, "belongs to", type(z))
print(y, "belongs to", type(y))

# Setting the specific data type
x = str("Hello World")    # str
y = int(20)               # int
z = float(20.5)           # float

# Converting data types
a = 10
b = 3.1
c = 1j
print(a, b, c)

a = float(a)   # int to float
b = complex(b)     # float to int
c = int(c.imag)  # complex to int
print(a, b, c)

# Specifying data types during conversion
x = str(5)      # x will be '5' (string)
y = int(3.99)   # y will be 3 (integer)
z = float("5.67") # z will be 5.67 (float)

# Random Number
import random
print(random.randrange(1, 10))  # Random number between 1 and 9
print(random.randint(1, 10))   # Random number between 1 and 10 (inclusive)
print(random.random())  # Random float between 0.0 and 1.0

### Strings ###

print("He is known as 'The King'")  # Using single quotes inside double quotes
print('She said "Hello!"')           # Using double quotes inside single quotes
print('It\'s a beautiful day!')       # Using escape character for single quote

# Escape characters
# \' - Single Quote
# \" - Double Quote
# \\ - Backslash
# \n - New Line
# \r - Carriage Return
# \t - Tab
# \b - Backspace
# \f - Form Feed
# \ooo - Octal value
# \xhh - Hex value
print("Hello\nWorld!")  
print("Hello\tWorld!")  
print("Hello\b World!")  

# Multiline strings – using triple quotes
multiline_str = """This is a
multiline string that spans
multiple lines."""
print(multiline_str)

# String indexing and slicing
a = "Hello"
print(a[1])      # Accessing character at index 1
print(a[0:4])
print(a(2:))   # From index 2 to end
print(a(-5:-2)) # From index -5 to -2

# Looping through a string
for x in "banana":
    print(x)

# String length
a = "Hello, World!"
print(len(a))
print(a.lower()) # Convert to lowercase
print(a.upper()) # Convert to uppercase
print(a.replace("H", "J")) # Replace character
b = a.split(",")  # Split string into list
print(b)

# Checking substring
txt = "The best things in life are free!"
print("free" in txt)  # Returns True
print("expensive" not in txt)  # Returns True

if "life" in txt:
    print("Ohhh yes, 'life' is present.")

# String concatenation
x = "Python"
y = "is"
z = "fun!"
print(x, y, z) 
print(x + " " + y + " " + z) 
print(x + y + z)      # No spaces

# F-strings (formatted string literals)
age = 18
txt = f"Alice is {age} years old."
print(txt)

# Modifiers (:) in f-strings
price = 20
txt = f"The price of the item is {price:.2f} euros."
print(txt)
txt1 = f"The price of the item is actually {price - 0.01:.2f} euros."
print(txt1)

# Some string methods
index("e")
print(f"The letter \"e\" is found at index {txt1.index('e')} in the string.")

isalpha(txt)
print(f"The string contains only alphabetic characters: \n{txt.isalpha()}")

upper(txt)
print(txt.upper())
print(f"I said: {txt.upper()}!!!")

### Boolean ###
print(19 > 9)   # True
print(19 == 9)  # False
print(19 < 9)   # False

a = 900
b = 232
if b > a:
    print("b is greater than a")
else:
    print("b is not greater than a")    

print(bool("Hi"))  # True, cause any string is True except empty ones
print(bool(0))     # False, cause any number is True except 0
print(bool([]))    # False, cause any collection is True except empty ones
def myFunction():
    return True
print(myFunction())  # True

# False values + object made from a class with __len__() returning 0
print(bool(False))
print(bool(None))
print(bool(0))
print(bool(""))
print(bool(()))
print(bool([]))
print(bool({}))
class myClass():
    def __len__(self):
        return 0
myobj = myClass()
print(bool(myobj))  # False

# Print "Ohhh yes" if the function returns True, otherwise print "Hell, no"
def myFunction2():
    return True
if myFunction2():
    print("Ohhh yes")
else:
    print("Hell, no")   

# Check if an object is an integer or not
x = 99
print(isinstance(x, bool))
