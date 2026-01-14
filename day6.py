### While Loops ###
# Print i as long as i is less than a given value
i = 3
while i < 9:
    print(i)
    i += 2 # remember to increment i, or else the loop will continue forever

i = 1
while i < 6:
    print(i)
    if i == 3:
        break #exits the loop when i is 3, even if followed by an else
    i += 1

i = 0
while i < 7:
    i += 1
    if i == 3:
        continue #stops the current iteration and skips to the next
    print(i)

i = 2
while i < 8:
    print(i)
    i += 1
else: # to run a block of code once the while condition is no longer true
    print("i is no longer less than 8")

### For Loops ###
# Print each fruit in a fruit list
fruits = ["apple", "pear", "pineapple"]
for x in fruits:
    print(x)

# Loops through strings
for x in "banana":
    print(x)
# funny thing
word = "banana"
for i in range(len(word)):
    print(word[i:])

# Break statement (which doesn't even execute the else block)
for x in fruits:
    print(x)
    if x == "pear": # to exit the loop
        break
for x in fruits:
    if x == "pear":
        break #break before the print 
    print(x)

# Continue statement
for x in fruits:
    if x == "pear":
        continue #not to print pear
    print(x) 

#The range() function
for x in range(5):
    print(x) #starts from 0 and increments by 1 by default, with value not included

for x in range(2, 6):
    print(x) #from 2 to 6 (not included)

for x in range(2, 20, 2):
    print(x) #incremented by 3 instead of default 1

# Else in For Loops
#Print all numbers from 0 to 5, and print a message when loop ends
for x in range(6):
    print(x)
else:
    print("Finished!")

# Nested Loops
#Print each adjective for every fruit
adj = ["red", "yellow", "juicy"]
fruits = ["apple", "banana", "cherry"]
for x in adj:
    for y in fruits:
        print(x, y)

# Pass statement
for x in [0, 1, 2]:
    pass #to avoid getting an error if no content loop



