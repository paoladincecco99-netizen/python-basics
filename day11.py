### JSON ###
import json #built-in package

# Convert from JSON to Python
x = '{"name":"Jack", "age":30, "city":"New York"}' #JSON
y = json.loads(x) #parse x
print(y["name"]) #Python dictionary as a result

# Convert from python to JSON
x = { #Python object (dict)
    "name": "Jack",
    "age": 30,
    "city": "New York"
}
y = json.dumps(x)
print(y) #JSON string

# Convert Python objects into JSON strings
print(json.dumps({"name": "John", "age": 30})) #dictionary
print(json.dumps(["apple", "banana"])) #list
print(json.dumps(("berries", "mangoes"))) #tuple
print(json.dumps("hello")) #string
print(json.dumps(33)) #int
print(json.dumps(33.3)) #float
print(json.dumps(True))
print(json.dumps(None))

# Format the result with indentations and line breaks and sort results
json.dumps(x, indent=4, separators=(". ", " = "), sort_keys=True)

### RegEX ###
import re #built-in package
txt = "The rain in Spain"

x = re.search("^The.*Spain$", txt) #if it starts with the and ends with spain
print(x)

x = re.findall("ai", txt) #returns a list containing all matches
print(x)

y = re.findall("Porto", txt)
print(y)

z = re.search("\s", txt)
print("The frist white-space character is located in position:", x.start())

a = re.split("\s", txt) #splits at each white-space character
print(a)
b = re.split("\s", txt, 1) #same but only at the first occurence
print(b)

c = re.sub("\s", "8", txt) #substitutes every white-space with "8"
print(c)
d = re.sub("\s", "8", txt, 2) #same but only first two occurences
print(d)

# Match Object
e = re.search("ai", txt)
print(e) #prints an object

f = re.search(r"\bS\w+", txt)
print(f.span()) #returns a tuple containing start and end position of match

g = re.search(r"\bS\w+", txt) 
print(g.string) #returns the string passed into the function

h = re.search(r"\bS\w+", txt)
print(h.group()) #returns the part of the string where there was a match