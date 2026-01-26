# Using packages
import cowsay 
cowsay.cow("Goooood Mooooorning")

### OOP demonstrations ###
class MyClass: #creating a class
    x = 7

o1 = MyClass() #creating an object
print(o1.x) #printing the value of x

del o1 #deleting an object

o1 = MyClass()
o2 = MyClass()
o3 = MyClass()
print(o1.x)
print(o2.x)
print(o3.x)

class Person:
    pass #for todos – since class definitions cannot be empty

#__init__() Method
class Person:
    def __init__(self, name, age): #to assign values to object properties
        self.name = name #accessing properties of the object
        self.age = age 
p1 = Person("Emil", 33)
p2 = Person("Linus", 24)
print(p1.name)
print(p1.age)
#it would otherwise be
class Person:
    pass
p1 = Person()
p1.name = "Tobias"
p1.age = 25
print(p1.name)
print(p1.age)

# Default values
class Person:
    def __init__(self, name, age=21):
        self.name = name
        self.age = age
p1 = Person("Emil")
p2 = Person("Tobias", 24)
print(p1.name, p1.age)
print(p2.name, p2.age)

#Self Parameter
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def greet(self): #to access properties and methods belonging to the class
        print("Hello, my name is " + self.name)
p1 = Person("Paul", 21)
p1.greet()

class Person:
    def __init__(self, name):
        self.name = name 
    def printname(self):
        print(self.name) #links the method to the specific object
p1 = Person("Tommy")
p1.printname()

class Person:
    def __init__(myobject, name, age): #it can also be called something else
        myobject.name = name
        myobject.age = age
    def greet(abc):
        print("Hello, my name is " + abc.name)
p1 = Person("Jack", 44)
p1.greet()

# Accessing properties
class Car:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year
    def display_info(self):
        print(f"{self.year} {self.brand} {self.model}")
car1 = Car("Toyota", "Corolla", 2020)
car1.display_info()

# Calling methods with self
class Person:
    def __init__(self, name):
        self.name = name
    def greet(self):
        return "Hello " + self.name
    def welcome(self):
        message = self.greet() #calling one method from another method
        print(message + "! Welcome here.")
p1 = Person("Tom")
p1.welcome 

#Properties
class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

p1 = Person("Tobias", 25)
print(p1.age)

p1.age = 26 #modifying property
print(p1.age)

del p1.age #deleting property

class Person:
  species = "Human" #Class property

  def __init__(self, name):
    self.name = name #Instance property

p1 = Person("Emil")
p2 = Person("Tobias")

print(p1.name)
print(p2.name)
print(p1.species)
print(p2.species)

Person.species = "Only Human" #changing a class property
p1.name = "Johnny" #changing an instance property
p1.age = 24 #adding a new property to an object

#Class Methods
class Person:
    def __init__(self, name):
        self.name = name
    def greet(self): #method
        print("Hello, my name is " + self.name)
p1 = Person("Emil")
p1.greet()

class Calculator: 
    def add(self, a, b): #method with parameters
        return a + b
calc = Calculator()
print(calc.add(3, 4))

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def get_info(self): #method that...
        return f"{self.name} is {self.age} years old" #accesses object properties
p1 = Person("Tobias", 19)
print(p1.get_info())

class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def celebrate_birthday(self): #method that...
    self.age += 1 #changes a property value
    print(f"Happy birthday! You are now {self.age}")

p1 = Person("Linus", 25)
p1.celebrate_birthday()
p1.celebrate_birthday()

#__str__() Method
class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def __str__(self): #to control what is returned when object is printed
    return f"{self.name} ({self.age})"

p1 = Person("Tobias", 36)
print(p1)

# Multiple methods can coexist within a class
class Playlist:
  def __init__(self, name):
    self.name = name
    self.songs = []

  def add_song(self, song):
    self.songs.append(song)
    print(f"Added: {song}")

  def remove_song(self, song):
    if song in self.songs:
      self.songs.remove(song)
      print(f"Removed: {song}")

  def show_songs(self):
    print(f"Playlist '{self.name}':")
    for song in self.songs:
      print(f"- {song}")

my_playlist = Playlist("Favorites")
my_playlist.add_song("Bohemian Rhapsody")
my_playlist.add_song("Stairway to Heaven")
my_playlist.show_songs()

del Playlist.remove_song #to delete a method
