### If... Else Statements ###
a = 33
b = 200
if b > a:
    print(f"{b} is greater than {a}") #note the indentatiom

# Multiple statements
age = 20
if age >= 18:
    print("You are an adult.")
    print("You can vote.")
    print("You have full legal rights.")

# Using Variables in conditions
is_logged_in = True 
if is_logged_in: #boolean variable used in condition without comparison
    print("Welcome back, user!")

# Elif Statement (for mutually exclusive conditions):
# it evaluates conditions from top to bottom, stops at first true condition 
a = 33
b = 33
if b > a:
    print(f"{b} is greater than {a}")
elif a == b:
    print(f"{a} and {b} are equal")

# Multiple Elif Statements
score = 85
if score >= 90:
    print("Grade: A")
elif score >= 80:
    print("Grade: B")
elif score >= 70:
    print("Grade: C")

# Day of the week checker example
day = 2
if day == 1:
    print("Monday")
elif day == 2:
    print("Tuesday")
elif day == 3:
    print("Wednesday")
elif day == 4:
    print("Thursday")
elif day == 5:
    print("Friday")
elif day == 6:
    print("Saturday")
elif day == 7:
    print("Sunday")

# Else Statement (for all other cases)
a = 200
b = 33
if b > a:
    print(f"{b} is greater than {a}")
elif a == b:
    print(f"{a} and {b} are equal")
else:
    print(f"{a} is greater than {b}")
# Without elif
if b > a:
    print(f"{b} is greater than {a}")
else:
    print(f"{a} is greater than {b}")

number = 7
if number % 2 == 0:
    print(f"{number} is even.")
else:
    print(f"{number} is odd.")

username = "Paola"
if  len(username) > 0:
    print(f"Hello, {username}!")
else:
    print("Error: No username provided.")

# Shorthand if
a = 2
b = 330
if a < b: print(f"{a} is less than {b}") # note the colon

# Shorthand if...else
a = 330
b = 33
print(f"{a} is less than {b}") if a < b else print(f"{a} is not less than {b}")
#OR
bigger = a if a > b else b
print(bigger, "is bigger.")

# Multiple conditions in one line
print("A") if a > b else print ("=") if a == b else print("B")

# Practical Examples
#Finding the maximum of two numbers
x = 15
y = 25
max_value = x if x > y else y
print("The maximum value is:", max_value)

#Setting a default value
username = ""
display_name = username if username else "Guest"
print("Welcome,", display_name)

# Logical Operators (and, or, not)
# Using 'and' operator
x = 5
y = 10
z = 15
if x < y and y < z:
    print(x, "is the smallest number.")

# Using 'or' operator
day = "Saturday"
if day == "Saturday" or day == "Sunday":
    print("It's the weekend!")

# Using 'not' operator
is_raining = False
if not is_raining:
    print("It's a sunny day, let's go outside!")

# Combining multiple logical operators
age = 25
has_id = True
if (age < 18 or age > 65) and has_id: #note the parentheses
    print("You are allowed to enter the club.")

# Nested If Statements – from the outermost condition inward
num = 10
if num > 0:
    if num % 2 == 0:
        print(f"{num} is a positive even number.")
    else:
        print(f"{num} is a positive odd number.")
else:
    print(f"{num} is not a positive number.")

# Nested vs. Logical Operators
# Nested If
temperature = 25
is_sunny = True
if temperature > 20:
    if is_sunny:
        print("It's a warm and sunny day!")
    else:
        print("It's warm but not sunny.")

# Using Logical Operators
if temperature > 20 and is_sunny:
    print("It's a warm and sunny day!")
elif temperature > 20 and not is_sunny:
    print("It's warm but not sunny.")

# Pass Statement
# Using pass in an empty if statement
num = 10
if num > 0:
    pass  # Placeholder for future code
# Example
age = 17
if age >= 18:
    print("You are an adult.")
else:
    pass  #TODO: Handle underage case later

### Match ###
# Used to perform different actions based on different conditions
# Syntax
match expression:
    case x:
        code block 
    case y:
        code block 
    case z:
        code block 

# Example with weekdays
day = 4
match day:
    case 1:
        print("Monday")
    case 2:
        print("Tuesday")
    case 3:
        print("Wednesday")
    case 4:
        print("Thursday")
    case 5:
        print("Friday")
    case 6:
        print("Saturday")
    case 7:
        print("Sunday")

day = 4
match day:
    case 6 | 7:
        print("It's the weekend!")
    case _: # default value
        print("Looking forward to the Weekend...")

month = 5
day = 3
match day:
    case 1|2|3|4|5 if month == 4:
        print("A weekday in May")
    case 6|7:
        print("A weekend in May")
    case _:
        print("No match")
