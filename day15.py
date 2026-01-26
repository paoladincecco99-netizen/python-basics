### Encapsulation ###
# Private Properties
class Person:
    def __init__(self, name, age):
        self.name = name
        self.__age = age #__ makes a property private to prevent accidental changes and...
p1 = Person("Paul", 23)
print(p1.name)
print(p1.__age) #Error ...to hide internal details

class Person:
    def __init__(self, name, age):
        self.name = name
        self.__age = age
    def get_age(self):
        return self.__age #getter method for private property
p1 = Person("John", 22)
print(p1.get_age())

class Person:
    def __init__(self, name, age):
        self.name = name
        self.__age = age
    def get_age(self):
        return self.__age
    def set_age(self, age): #setter method to modify a private property
        if age > 0: #to validate the value before setting it (not necessary)
            self.__age = age
        else:
            print("Age must be positive")

p1 = Person("Tommy", 25)
print(p1.get_age())
p1.set_age(26) #modifying a private property
print(p1.get_age()) #getting the modified private property

#Other example
class Student:
    def __init__(self, name):
        self.name = name
        self.__grade = 0 #__ to make it private
    def set_grade(self, grade): #to later motify it
        if 0 <= grade <= 100:
            self.__grade = grade
        else: 
            print("Grade must be between 0 and 100")
    def get_grade(self): #to get a private property
        return self.__grade 
    def get_status(self):
        if self.__grade >= 60:
            return "Passed"
        else:
            return "Failed"

student1 = Student("Johnny")
student1.set_grade(88)
print(student1.get_status())
print(student1.get_grade())

# Protected Properties
class Person:
    def __init__(self, name, salary):
        self.name = name
        self._salary = salary #to protect the property

worker1 = Person("William", 30000)
print(worker1.name)
print(worker1._salary) # can access but shouldn't, since _ is just a convention

# Private Methods
class Calculator:
    def __init__(self):
        self.result = 0
    def __validate(self, num): #private method
        if not isinstance(num, (int, float)):
            return False
        return True
    def add(self, num):
        if self.__validate(num):
            self.result += num
        else:
            print("Invalid number")

calc = Calculator()
calc.add(10)
calc.add(5)
print(calc.result) 

### Inner Classes ###
class Outer:
    def __init__(self):
        self.name = "Outer Class"
    class Inner:
        def __init__(self):
            self.name = "Inner Class"
        def display(self):
            print("This is the inner class")
outer = Outer()
inner = outer.Inner() #to access the inner class from the outside
inner.display()
print(outer.name)

class Outer:
    def __init__(self):
        self.name = "Outer Class"
    class Inner:
        def __init__(self, outer):
            self.outer = outer
        def display(self):
            print(f"Outer class name: {self.outer.name}")
outer = Outer()
inner = outer.Inner(outer) #to access the outer from the inner
inner.display()

#Example
class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
        self.engine = self.Engine()
    class Engine:
        def __init__(self):
            self.status = "Off"
        def start(self):
            self.status = "Running"
            print("Engine started")
        def stop(self):
            self.status = "Off"
            print("Engine stopped")
    def drive(self):
        if self.engine.status == "Running":
            print(f"Driving the {self.brand} {self.model}")
        else: 
            print("Start the engine first!")
car = Car("Toyota", "Corolla")
car.drive()
car.engine.start()
car.drive()

# Multiple inner classes
class Computer:
    def __init__(self):
        self.cpu = self.CPU() #creating objects within outer class...
        self.ram = self.RAM() #...defined in inner classes
    class CPU:
        def process(self):
            print("Processing data...")
    class RAM:
        def store(self):
            print("Storing data...")
computer = Computer()
computer.cpu.process() #accessing the inner class and its method
computer.cpu.store() #same here

