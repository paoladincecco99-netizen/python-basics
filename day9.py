### Recursion ###
def countdown(n):
    if n <= 0:
        print("Done!")
    else:
        print(n)
        countdown(n - 1)

countdown(5)

def factorial(n):
    if n == 0 or n == 1: #base case
        return 1
    else: #recursive case
        return n * factorial(n - 1)

print(factorial(5))

# Fibonacci sequence
def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)
print(fibonacci(7)) #to find the 7th element 

# Recursion with lists
def sum_list(numbers):
    if len(numbers) == 0:
        return 0
    else:
        return numbers[0] + sum_list(numbers[1:])
my_numbers = [1, 2, 3, 4, 5]
print(sum_list(my_numbers))

def find_max(numbers):
    if len(numbers) == 1:
        return numbers[0]
    else:
        max_of_rest = find_max(numbers[1:])
        return numbers[0] if numbers[0] > max_of_rest else max_of_rest
my_numbers = [4, 7, 2, 9, 1]
print(find_max(my_numbers))

#Check recursion limit – increasing it can cause crashes
import sys
print(sys.getrecursionlimit())

### Generators ###
#Functions that can pause and resume their execution
#When called, it returns a generator object, which is an iterator
#Its code is only compiled, not executed yet 
# – it only executes when iterated over the generator

def my_generator():
    yield 1 #yield so that the function's state is saved
    yield 2 # and the value is returned
    yield 3 # next time the generator is called, it continues from where it left off
for value in my_generator():
    print(value)

def count_up_to(n):
    count = 1
    while count <= n:
        yield count #unlike return, yield pauses the function and can be called multiple times
        count += 1
for num in count_up_to(5):
    print(num)

def large_sequence(n):
    for i in range(n):
        yield i
gen = large_sequence(1000000) #...this doesn't create a million numbers in memory...
print(next(gen)) #next() to manually iterate through a generator
print(next(gen))
print(next(gen)) 
#...when there will be no more values to yield, 
# the generator will raise a StopIteration exception

# Generators expressions
gen_exp = (x * x for x in range(3))
print(gen_exp)
print(list(gen_exp))

#Calculates sum of squares w/o creating a list
total = sum(x * x for x in range(10))
print(total) 

#Fibonacci sequence generator
def fibonacci():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b
gen = fibonacci()
for _ in range(100):
    print(next(gen))

# Generator Methods send() and close()
def echo_gen():
    while True:
        received = yield
        print("Received:", received)
gen = echo_gen()
next(gen) #to prime the generator
gen.send("Hello") #to send a value to the generator
gen.send("Everyone")

def my_gen():
    try:
        yield 1
        yield 2
        yield 3
    finally:
        print("Generator closed")
gen = my_gen()
print(next(gen))
gen.close() #to stop the generator


