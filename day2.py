### Operators ###
# Arithmetic Operators: +, -, *, /, %, **, // 
x = 25
y = 4

print(x + y)
print(x % y) # Modulus operator returns the remainder of division
print(x ** y) # Exponentiation operator raises x to the power of y
print(x // y) # Floor division operator returns the largest integer less than or equal to the division result

# Assignment Operators: =, +=, -=, *=, /=, %=, **=, //=
a = 10
a += 5  # Equivalent to a = a + 5
a -= 3  # Equivalent to a = a - 3
a += 2  # Equivalent to a = a * 2
a /= 2  # Equivalent to a = a / 2
a %= 3  # Equivalent to a = a % 3
a **= 2 # Equivalent to a = a ** 2
a //= 2 # Equivalent to a = a // 2
a &= 1  # Equivalent to a = a & 1
a |= 2  # Equivalent to a = a | 2
a ^= 3  # Equivalent to a = a ^ 3
a >>= 1 # Equivalent to a = a >> 1
a <<= 2 # Equivalent to a = a << 2
print(x := y) # Comparison operator checks if x is equal to y

# Walrus Operator: :=
# The walrus operator allows assignment within an expression
numbers = [1, 2, 3, 4, 5]
count = len(numbers)
if count > 3:
    print(f("This list has {count} elements."))
# OR, using the walrus operator to combine assignment and condition check
if (count := len(numbers)) > 3:
    print(f"This list has {count} elements.")

# Comparison Operators: ==, !=, >, <, >=, <=
# Returns a boolean value based on the comparison
# Chain comparison with multiple operators or logical operators ('and', 'or', 'not')
x = 10
print(x > 5 and x < 15)  # True
print(x == 10 or x == 20) # True
print(not(x != 10))      # True

# Identity Operators: is, is not
# Check if two variables point to the same object in memory
# Different from == which checks for value equality
x = [1, 2, 3]
y = [4, 5, 6]
z = x
print(x is z)      # True, because z points to the same object as x
print(x is y)  # False, because x and y point to different objects
print(x is not y)  # True, because x and y point to different objects

# Membership Operators: in, not in
# Check if a value is present in a sequence (like a list, tuple, or string
names = ["Alice", "Bob", "Charlie"]
print("Alice" in names)      # True
print("David" not in names)  # True
print("li" in "Alice")       # True
print("zz" in "Bob")     #  False

#Bitwise Operators: &, |, ^, ~, <<, >>
# Perform bit-level operations on integers
&# Bitwise AND
|# Bitwise OR
^# Bitwise XOR – returns 1 if only one of the bits is 1
~# Bitwise NOT – inverts all the bits
<<# Left Shift – shifts bits to the left, adding zeros on the right
>># Right Shift – shifts bits to the right, discarding bits on the right

a = 10  # In binary: 1010
b = 4   # In binary: 0100
print(a & b)  # Bitwise AND: 0000 (0 in decimal)
print(a | b)  # Bitwise OR: 1110 (14 in decimal)
print(a ^ b)  # Bitwise XOR: 1110 (14 in decimal)
print(~a)     # Bitwise NOT: -1011 (-11 in decimal, two's complement)
print(a << 2) # Left Shift: 101000 (40 in decimal)
print(a >> 2) # Right Shift: 0010 (2 in decimal)

# Precedence Order of Operators
# 1. Parentheses ()
# 2. Exponentiation **
# 3. Unary plus and minus +x, -x, bitwise NOT ~x
# 4. Multiplication, Division, Floor Division, Modulus *, /, //,
# 5. Addition and Subtraction +, -
# 6. Bitwise Shifts <<, >>
# 7. Bitwise AND &
# 8. Bitwise XOR ^
# 9. Bitwise OR |
# 10. Comparison Operators ==, !=, >, <, >=, <=
# 11. Identity Operators is, is not
# 12. Membership Operators in, not in
# 13. Logical NOT not
# 14. Logical AND and OR and, or
# 15. Assignment Operators =, +=, -=, *=, /=, %=, **
# 16. Walrus Operator :=

### Lists ###
firstList = [1, 2, 3, 4, 5]
print(type(firstList))  # Output: <class 'list'>
print(len(firstList))   # Output: 5

# List construction
secondList = list((6, 7, 8, 9, 10)) # note the double parentheses
print(secondList)  # Output: [6, 7, 8, 9, 10]

# Accessing list elements
print(firstList[0])    # Output: 1 (first element)
print(firstList[-1])   # Output: 5 (last element)
print(firstList[1:4])  # Output: [2, 3, 4] (slicing from index 1 to 3)
print(firstList[:3])   # Output: [1, 2, 3] (slicing from start to index 2)
print(firstList[2:])   # Output: [3, 4, 5] (slicing from index 2 to end)
print(firstList[:])    # Output: [1, 2, 3, 4, 5] (entire list)
print(firstList[::2])  # Output: [1, 3, 5] (every second element)
print(firstList[::-1]) # Output: [5, 4, 3, 2, 1] (reversed list)
if 3 in firstList:
    print("3 is present in the list")

# Modifying list elements
firstList[0] = 10
print(firstList)  # Output: [10, 2, 3, 4, 5]

firstList[1:3] = [20, 30]
print(firstList)  # Output: [10, 20, 30, 4, 5]

firstList[3:4] = [50, 60, 70]
print(firstList)  # Output: [10, 20, 30, 50, 60, 70, 5]

firstList[2:3] = []
print(firstList)  # Output: [10, 20, 50, 60, 70, 5]

firstList.insert(2, 33)
print(firstList)  # Output: [10, 20, 33, 50, 60, 70, 5]

firstList.append(75) 
print(firstList)  # Output: [10, 20, 33, 50, 60, 70, 5, 75]

newList = firstList.copy()
newList.extend(secondList)
print(newList)  # Output: [10, 20, 33, 50, 60, 70, 5, 75, 6, 7, 8, 9, 10]

firstTuple = (100, 200, 300)
firstList.extend(firstTuple)
print(firstList)  # Output: [10, 20, 33, 50, 60, 70, 5, 75, 100, 200, 300]

firstList.remove(33)
print(firstList)  # Output: [10, 20, 50, 60, 70, 5, 75, 100, 200, 300]

firstList.pop(1) # Removes element at index 1
print(firstList)  # Output: [10, 50, 60, 70, 5, 75, 100, 200, 300]
# If no index is specified, removes the last element

del firstList[2] # Deletes element at index 2
print(firstList)  # Output: [10, 50, 70, 5, 75, 100, 200, 300]
# You can also use del to delete the entire list

firstList.clear() # Empties the list
print(firstList)  # Output: []

# For loop through a list
thisList = ["a", "b", "c"]
for item in thisList:
    print(item)
# To print all items referring to their index position
for index in range(len(thisList)):
    print(thisList[index])

# While loop through a list
i = 0 # Initialize index
while i < len(thisList): # len() to determine the lenghth of the list
    print(f"Item of the list: {thisList[i]}") # Access each item using the index
    i += 1 # Increment index to avoid infinite loop

# List comprehension
squares = [x**2 for x in range(4)]
print(f"Squares of numbers from 0 to 3: {squares}")
# The syntax for list comprehension is:
# newList = [expression for item in iterable if condition == True]
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newList = [x for x in fruits if "a" in x]
print(f"Fruits containing 'a': {newList}")

newerList = [x for x in fruits if x != "apple"]
print(f"Fruits excluding 'apple': {newerList}")

evenNewerList = [x for x in range(10)] #to create an iterable
evenNewerList = [x for x in range(10) if x < 5]
print(f"Numbers less than 5: {evenNewerList}")

NewList = [x.upper() for x in fruits]
print(f"Fruits in uppercase: {NewList}")

NewList1 = [x if x != "banana" else "orange" for x in fruits]
print(f"Replacing 'banana' with 'orange': {NewList1}")

fruits.sort()
print(fruits) # Sorts the list in ascending order

fruits.sort(reverse=True)
print(fruits) # Sorts the list in descending order

# Custom sort using a function
def myFunc(n):
    return abs(n - 50)

qstList = [100, 50, 65, 82, 23]
qstList.sort(key=myFunc)
print(f"Custom sorted list: {qstList}") # Sorts based on the distance from 50



