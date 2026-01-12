# Copy lists
thisList = ["one", "two", "three"]
newList = thisList.copy()
print(newList)

newerList = list(thisList)
print(newerList)

evenNewerList = thisList[:]
print(evenNewerList)

# Join lists
list1 = ["a", "b", "c"]
list2 = [1, 2, 3]
joinedList = list1 + list2
print(joinedList)

for item in list2:
    list1.append(item)
print(list1)

list1.extend(list2)
print(list1)

### Python Tuples ###
thisTuple = ("apple", "banana", "cherry")
print(thisTuple)
print(len(thisTuple))

# One item tuple need a comma
oneItemTuple = ("apple",)
print(type(oneItemTuple))
notATuple = ("apple")

# Tuple items can be of any data type
mixedTuple = ("apple", 1, True, 3.14)
print(mixedTuple)
print(type(mixedTuple)) #<class 'tuple'>
print(type(mixedTuple[1])) #<class 'int'>

thisTuple = tuple(("apple", "banana", "cherry")) # note the double round-brackets
print(thisTuple)

# Access tuple items
print(thisTuple[1]) #banana
print(thisTuple[-1]) #cherry
print(thisTuple[1:3]) #('banana', 'cherry')

# Check if item exists
if "apple" in thisTuple:
    print("Yes, 'apple' is in the tuple")

# Update tuple - tuples are immutable, so we need to convert to a list first
x = ("apple", "banana", "cherry")
y = list(x) # convert to list
y[1] = "kiwi" # modify the list
y.append("orange") # add an item
y.remove("apple") # remove an item
x = tuple(y) # convert back to tuple
print(x)

# Add tuple to a tuple
z = ("orange",)
x += z
print(x)

# Delete tuple
del x
# print(x) # This will raise an error because x is deleted

# Unpack tuple
fruits = ("kiwi", "banana", "cherry")
(green, yellow, red) = fruits
print(green)  # kiwi
print(yellow) # banana
print(red)    # cherry

# Using Asterisk*
fruits = ("kiwi", "banana", "cherry", "strawberry", "raspberry")
(green, yellow, *red) = fruits
print(green)  # kiwi
print(yellow) # banana
print(red)    # ['cherry', 'strawberry', 'raspberry']
# Asterisk* with different position
# Python will assign values to the variable until 
# the number of values left matches the number of variables left.
(green, *red, yellow) = fruits
print(green)  # kiwi
print(yellow) # raspberry
print(red)    # ['banana', 'cherry', 'strawberry']

# Loop through tuple
thisTuple = ("father", "mother", "sister")
for item in thisTuple:
    print(item)

# Loop through tuple using index
for i in range(len(thisTuple)):
    print(thisTuple[i])

# While loop through tuple
i = 0
while i < len(thisTuple):
    print(thisTuple[i])
    i += 1

# Join tuples
tuple1 = ("a", "b", "c")
tuple2 = (1, 2, 3)
tuple3 = tuple1 + tuple2
print(tuple3)

# Multiply tuple
tuple1 = ("hello",)
tuple2 = tuple1 * 3
print(tuple2)   #('hello', 'hello', 'hello')

### Sets ###
thisSet = {"sugar", "salt", "pepper"}
print(thisSet)
set1 = {"abc", 33, True, 40.5} # set with mixed data types
set2 = set(("apple", "banana", "cherry")) # note the double round-brackets

for x in thisSet:
    print(x)

print("salt" in thisSet) #True
print("cumin" not in thisSet) #False
thisSet.add("cumin")
print("cumin" in thisSet) #True
set2.update(set1)
print(set2)
set2.remove(33) # raises error if item not found
set2.discard(100) # does not raise error if item not found
set1_2 = set1.pop() # removes and returns an arbitrary item
set1_2.clear() # removes all items
del set1_2 # deletes the set completely

# Add any iterable
set2.update(["kiwi", "mango"]) # adding list
print(set2)

# Loop through a set
for x in set2:
    print(x)

# Join sets
setA = {"a", "b", "c"}
setB = {"d", "e", "f"}
setC = {"g", "h", "i"}
list = [1,2,3]

setU = setA.union(setB)
setUU = setA.union(setB, setC)
#OR
setI = setA | setB
completeset = setA | setB | setC

print(setU) #{'a', 'b', 'c', 'd', 'e', 'f'}
print(setI) #{'a', 'b', 'c', 'd', 'e', 'f'}
print(setUU) #{'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i'}
print(completeset) #{'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i'}

setList = setB.union(list)
print(setList) #{1, 2, 3, 'd', 'e', 'f'}

# Intersection – return common items only
setX = {"a", "b", "c", "d"}
setY = {"c", "d", "e", "f"}
setZ = setX.intersection(setY)
#OR
setZ2 = setX & setY
print(setZ) #{'d', 'c'}
print(setZ2) #{'d', 'c'}

setX.intersection_update(setY) # keeps only the items that are present in both sets
print(setX) #{'d', 'c'}

# Difference – return items that are not present in both sets
setM = {"a", "b", "c", "d"}
setN = {"c", "d", "e", "f"}
setO = setM.difference(setN)
#OR
setO2 = setM - setN
print(setO) #{'a', 'b'}
print(setO2) #{'a', 'b'}
setM.difference_update(setN) # removes the items that are present in both sets from the setM
print(setM) #{'a', 'b'}

# Symmetric Difference – return items that are not present in both sets
setP = {"a", "b", "c", "d"}
setQ = {"c", "d", "e", "f"}
setR = setP.symmetric_difference(setQ)
#OR
setR2 = setP ^ setQ
print(setR) #{'a', 'b', 'e', 'f'}
print(setR2) #{'a', 'b', 'e', 'f'}
setP.symmetric_difference_update(setQ) # keeps only the items that are not present in both
print(setP) #{'a', 'b', 'e', 'f'}

# Frozen Sets
frozenSet = frozenset(["apple", "banana", "cherry"])
print(frozenSet)

### Dictionary ###
thisDict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964,
}
print(thisDict)
print(len(thisDict)) #3 (items)
print(thisDict["brand"]) #Ford

thisDict["year"] = 2020 #update value
thisDict["color"] = "red" #add item
thisDict["color"] = ["blue", "black"] #update value to list
thisDict.pop("color") #remove item
thisDict.popitem() #remove last inserted item
del thisDict["model"] #remove item
#del thisDict #delete dictionary completely
#thisDict.clear() #empty the dictionary
thisdict = dict(brand="Ford", model="Mustang", year=1964) #note the use of equals rather than colon for key/value pairs

# Access items
x = thisDict["brand"] #Ford
y = thisDict.get("model") #Mustang
number = thisDict.get("number") #None – no error if key does not exist
print(x)

# Get all keys
keys = thisDict.keys()
print(keys) #dict_keys(['brand', 'model', 'year', 'color'])
thisDict["owner"] = "John" #adding new item also updates keys view
print(keys) #dict_keys(['brand', 'model', 'year', 'color', 'owner'])

# Get all values
values = thisDict.values()
print(values) #dict_values(['Ford', 'Mustang', 2020, ['blue', 'black'], 'John'])
thisDict["year"] = 2021 #updating existing item also updates values view
#OR
thisDict.update({"year": 2021})
print(values) #dict_values(['Ford', 'Mustang', 2021, ['blue', 'black'], 'John'])

# Get all items
items = thisDict.items()
print(items) #dict_items([('brand', 'Ford'), ('model', 'Mustang'), ('year', 2021), ('color', ['blue', 'black']), ('owner', 'John')])
thisDict["color"] = "white" #updating existing item also updates items view
print(items) #dict_items([('brand', 'Ford'), ('model', 'Mustang'), ('year', 2021), ('color', 'white'), ('owner', 'John')])  

# Check if key exists
if "model" in thisDict:
    print("Yes, 'model' is one of the keys in the thisDict dictionary") 
#OR
if thisDict.get("model"):
    print("Yes, 'model' is one of the keys in the thisDict dictionary") 


# Loop through dictionary
for x in thisDict:
    print(x)  #prints all key names, one by one
    #OR
for x in thisDict.keys():
    print(x)

for x in thisDict.values():
    print(x)  #prints all values, one by one

for key in thisDict:
    print(key, thisDict[key]) #prints all key names and values, one by one
for x, y in thisDict.items():
    print(x, y) #prints all key names and values, one by one

# Copy dictionary
newDict = thisDict.copy() #using built-in method
#OR
newDict2 = dict(thisDict) #using built-in function

# Nested dictionaries
myFutureFamily = {
    "child1": {
        "name": "Emily",
        "year": 2027
    },
    "child2": {
        "name": "Michael",
        "year": 2030
    },
    "child3": {
        "name": "Sophie",
        "year": 2032
    }
}
print(myFutureFamily)

#OR
child1 = {
    "name": "Emily",
    "year": 2027
}
child2 = {
    "name": "Michael",
    "year": 2030
}
child3 = {
    "name": "Sophie",
    "year": 2032
}
myFutureFamily2 = {
    "child1": child1,
    "child2": child2,
    "child3": child3
}
print(myFutureFamily2)

# Accessing items in nested dictionary
print(myfamily["child2"]["name"]) #Michael
print(myFutureFamily2["child3"]["year"]) #2032

# Adding items in nested dictionary
myFutureFamily["child4"] = {
    "name": "James",
    "year": 2035
}

# Updating items in nested dictionary
myFutureFamily["child2"]["year"] = 2031
myFutureFamily2["child1"].update({"year": 2028})

# Another nested dictionary example
class_room = {
    "student1": {
        "name": "Alice",
        "age": 22,
        "skills": ["Python", "SQL"]
    },
    "student2": {
        "name": "Bob",
        "age": 24,
        "skills": ["Java", "C++"]
    }
}
#Accessing second skill of student 2 using value index
second_skill_st2 = class_room["student2"]["skills"][1] 


# Loops in nested dictionary – through all keys and values
for child, details in myFutureFamily.items(): # .items() method to get key-value pairs
    print(child.upper())  # prints child1, child2, child3 in upper case
    for key in details:
        print(key + ':', details[key]) # prints name and year for each child
        print() # just to add a blank line between children