# Introduction
print("Hello, World")
# Arithmetic operations 
print(22/7)
print(22//7) 
# Introduction to variables
a = 15
b = 25
print(a > 10 and b > 10)
a = 5
b = 20
print(a < 10 or b < 10)
a = 8
print(not(a == 10))
# For loop
for i in range(1, 11):
    print(i)
for i in range(1, 20):
    if i % 2 == 0:
        print(i, end=" ")
for i in range(2, 20, 2):
    print(i)
fruits = ["Orange", "Banana", "Apple"]
for fruit in fruits:
    print(fruit)
name = "Omenai Samuel"
for ch in name:
    print(ch)
# Strings 
string = "print"
print(string.startswith("print"))
print(string.endswith("print"))
print(string[0])
print(string[-1])
print(string[2])
print(name[::-1])
print(len("I love Python!"))
print("HELLO WORLD".lower())
print("  Python is awesome  ".strip())
print("This is a bad day".replace("bad", "good"))
print("one two three four".split(" "))
print("data science is amazing".count("a"))
# Lists
movies = ["Abbatoir", "Abejoye", "Snowden", "Curious George", "Ecanto"]
print(movies)
movies.append("Moana")
print(movies)
movies.insert(2, "The Hacker")
print(movies)
movies.remove("Curious George")
print(movies)
movies.sort()
print(movies)
n = [0, 1, 2, 3, 4, 5, 6]
print(n[::3])
# List comprehensions
movies_a = [movie for movie in movies if movie[0] == "A"]
print(movies_a)
# Tuples
fav_pro_lang = ("Python", "Java", "C++", "Javascript")
print(fav_pro_lang)
print(len((10, 20, 30, 40, 50)))
no = (5, 1, 5, 2, 5, 3, 5)
print(no.count(5))
programming_languages = ("Java", "Python", "C++", "Go")
print(programming_languages.index("Python"))
tuple = (1, 2, 3, 4, 5, 6)
print(tuple[::-1])
# Dictionaries
student = {
    "name" : "Samuel",
    "age" : 12,
    "course" : "Python"
}
student["age"] = 14
student["state"] = "Edo"
del student["course"]
print(student.get("age"))
print(student)
for key, value in student.items():
    print(key, ":", value)
# Dictionary comprehension
#squares = [x: x * x for x in range(1, 6)]
#print(squares)
# Sets
A = {1, 2, 3, 4}
B = {3, 4, 5, 6}
print(A | B)
print(A & B)
print(A - B)
print(B - A)
print(A ^ B)
print({3, 4} <= A)
print({2, 3} <= B)
print(A >= {1, 4})
# Sets comprehension
num = [x for x in range(1, 11) if x % 2 == 0]
print(num)
# Functions
def greet(name, grade, age):
    print(f"Hello {name}!")
    print(f"{name} is in {grade}")
    print(f"And {name} is {age} years old")
greet("Sam", "Grade 10", 14)
greet("Dave", "Grade 3", 7)
def multiply(a, b):
    return a * b
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
answer = multiply(a, b)
print(f"Answer = {answer}")
def area(length, breadth):
    return length * breadth  
length = int(input("Enter your length: "))
breadth = int(input("Enter your breadth: "))
print("Area =", area(length, breadth) )
def uppercase(func):
    def wrapper():
        orig_message = func()
        modified_message = orig_message.upper()
        return modified_message
    return wrapper
@uppercase
def greet():
    return "Welcome"
reall = greet()
print(reall)
#greet_upper = uppercase(greet)
#print(greet_upper)

@uppercase
def greett():
    return "i am sam"
real = greett()
print(real)
def greet(name):
    return "Hi " + name
def welcome(name, func):
    print(func(name))
    return func
welcome(input("Enter a name: "), greet)
# Match
day = 3
match day:
    case 1:
        print("Monday")
    case 2:
        print("Tuesday")
    case 3:
        print("Wednesday")
    case 4 | 5:
        print("Midweek")
    case _:
        print("Weekend")
# Args and Kwargs
def sum_all(*args):
    total = 0
    for num in args:
        total += num
    return total
sum_all(1, 2, 3, 4, 5)
def print_info(**kwargs):
    for key, value in kwargs.items():
        print(f"{key} : {value}")
print_info(Name = "Alice", Age = 25, City = "New York")
def uppercase(func):
    def wrapper():
        orig_message = func()
        modified_message = orig_message.upper()
        return modified_message
    return wrapper
def lowercase(func):
    def wrapper():
        orig_message = func()
        modified_message = orig_message.lower()
        return modified_message
    return wrapper
#@lowercase
@uppercase
def greett():
    return "Welcomee"
real = greett()
print(real)
def greet(name):
    return "Hi " + name
def welcome(name, func):
    print(func(name))
    return func
welcome(input("Enter a name: "), greet)
list = [2, 4, "Sam"]
tuple = (2, 4, "Sam")
set = {2, 2, 4, "Sam"}
dict = {2: 2, "Sam": 14}
print(list, tuple, set, dict)