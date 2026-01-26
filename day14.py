### Inheritance ###
# Creating a parent class
class Person:
    def __init__(self, fname, lname):
        self.firstname = fname
        self.lastname = lname
    def printname(self):
        print(self.firstname, self.lastname)
x = Person("John", "Travolta")
x.printname()

# Creating a child class
class Student(Person): #sending the parent as parameter
    def __init__(self, fname, lname): #to add properties etc...
        Person.__init__(fname, lname) #to keep inheritance of parent instead of overriding
#OR
class Student(Person): #sending the parent as parameter
    def __init__(self, fname, lname): 
        super.__init__(fname, lname) #to automatically keep inheritance of parent
x = Student("Mike", "Buongiorno")
x.printname()

# Adding properties
class Student(Person):
    def __init__(self, fname, lname):
        super().__init__(fname, lname)
        self.graduationyear = 2021 #2021 variable passed into the student class

class Student(Person):
    def __init__(self, fname, lname, year):
        super().__init__(fname, lname)
        self.graduationyear = year
x = Student("Mike", "Wheeler", 2025)

# Adding Methods
class Student(Person):
    def __init__(self, fname, lname, year):
        super().__init__(fname, lname)
        self.graduationyear = year
    def welcome(self):
        print("Welcome", self.firstname, self.lastname, "to the class of", self.graduationyear)

### Polymorphism ###
x = "helloooo"
print(len(x)) #for strings, it returns no of characters

mytuple = ("apple", "pine", "pineapple")
print(len(mytuple)) #for tuples, it returns no of items

thisdict = {
    "brand": "Fiat",
    "model": "500",
    "year": 2021
}
print(len(thisdict)) #for dictionaries, it returns no of key/value pairs

# Class polymorphism
#Same method, different classes
class Car:
  def __init__(self, brand, model):
    self.brand = brand
    self.model = model

  def move(self):
    print("Drive!")

class Boat:
  def __init__(self, brand, model):
    self.brand = brand
    self.model = model

  def move(self):
    print("Sail!")

class Plane:
  def __init__(self, brand, model):
    self.brand = brand
    self.model = model

  def move(self):
    print("Fly!")
car1 = Car("Ford", "Kuga") #creating a car object
boat1 = Boat("Ibiza", "Touring 20") #creating a boat object
plane1 = Plane("Boeing", "747") #creating a place object

for x in (car1, boat1, plane1):
   x.move()

# Inheritance Class Polymorphism
class Vehicle:
   def __init__(self, brand, model):
      self.brand = brand
      self.model = model
   def move(self):
      print("Move!")
#Children will inherit but can override methods
class Car(Vehicle):
   pass
class Boat(Vehicle):
  def move(self):
    print("Sail!")

class Plane(Vehicle):
  def move(self):
    print("Fly!")

car1 = Car("Ford", "Mustang")       
boat1 = Boat("Ibiza", "Touring 20") 
plane1 = Plane("Boeing", "747")  

for x in (car1, boat1, plane1):
   print(x.brand)
   print(x.model)
   x.move()

