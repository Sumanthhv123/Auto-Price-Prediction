# Complete Python Learning Guide 🐍

Welcome to your comprehensive Python learning journey! This guide will take you from absolute beginner to advanced Python programmer.

## Table of Contents
1. [Getting Started](#getting-started)
2. [Python Basics](#python-basics)
3. [Data Types and Variables](#data-types-and-variables)
4. [Operators](#operators)
5. [Control Structures](#control-structures)
6. [Functions](#functions)
7. [Data Structures](#data-structures)
8. [Object-Oriented Programming](#object-oriented-programming)
9. [File Handling](#file-handling)
10. [Error Handling](#error-handling)
11. [Modules and Packages](#modules-and-packages)
12. [Advanced Topics](#advanced-topics)
13. [Popular Libraries](#popular-libraries)
14. [Practice Projects](#practice-projects)
15. [Best Practices](#best-practices)

---

## Getting Started

### What is Python?
Python is a high-level, interpreted programming language known for its:
- Simple and readable syntax
- Versatility (web development, data science, AI, automation)
- Large ecosystem of libraries
- Strong community support

### Installing Python
```bash
# Check if Python is installed
python3 --version

# Install Python on Ubuntu/Debian
sudo apt update
sudo apt install python3 python3-pip

# Install Python on other systems
# Visit https://python.org/downloads/
```

### Running Python Code
```bash
# Interactive mode
python3

# Run a Python file
python3 script.py

# Using Jupyter Notebook
pip3 install jupyter
jupyter notebook
```

---

## Python Basics

### Your First Python Program
```python
# This is a comment
print("Hello, World!")  # This prints text to the console

# Multi-line comments
"""
This is a multi-line comment
You can write multiple lines here
"""
```

### Python Syntax Rules
- Python uses indentation (spaces/tabs) to define code blocks
- No semicolons needed at the end of statements
- Case-sensitive (variable `name` is different from `Name`)
- Use 4 spaces for indentation (PEP 8 standard)

---

## Data Types and Variables

### Variables
```python
# Variables don't need to be declared with a specific type
name = "Alice"          # String
age = 25               # Integer
height = 5.6           # Float
is_student = True      # Boolean

# Dynamic typing - you can change variable types
age = "twenty-five"    # Now age is a string

# Multiple assignment
x, y, z = 1, 2, 3
a = b = c = 10
```

### Basic Data Types

#### 1. Numbers
```python
# Integers
count = 42
negative = -17

# Floats
price = 19.99
temperature = -5.5

# Complex numbers
complex_num = 3 + 4j

# Type conversion
num_str = "123"
num_int = int(num_str)      # Convert to integer
num_float = float(num_str)  # Convert to float
```

#### 2. Strings
```python
# String creation
single_quotes = 'Hello'
double_quotes = "World"
triple_quotes = """This is a
multi-line string"""

# String operations
first_name = "John"
last_name = "Doe"
full_name = first_name + " " + last_name  # Concatenation

# String formatting
age = 30
message = f"I am {age} years old"  # f-string (Python 3.6+)
message2 = "I am {} years old".format(age)  # .format() method
message3 = "I am %d years old" % age  # % formatting (older style)

# String methods
text = "  Hello World  "
print(text.strip())        # Remove whitespace: "Hello World"
print(text.lower())        # Lowercase: "  hello world  "
print(text.upper())        # Uppercase: "  HELLO WORLD  "
print(text.replace("World", "Python"))  # "  Hello Python  "
print(len(text))           # Length: 15

# String indexing and slicing
word = "Python"
print(word[0])     # First character: 'P'
print(word[-1])    # Last character: 'n'
print(word[1:4])   # Slice: 'yth'
print(word[:3])    # First 3 chars: 'Pyt'
print(word[3:])    # From index 3: 'hon'
```

#### 3. Booleans
```python
is_valid = True
is_empty = False

# Boolean operations
result = True and False  # False
result = True or False   # True
result = not True        # False

# Comparison returns boolean
is_equal = (5 == 5)      # True
is_greater = (10 > 5)    # True
```

---

## Operators

### Arithmetic Operators
```python
a, b = 10, 3

print(a + b)    # Addition: 13
print(a - b)    # Subtraction: 7
print(a * b)    # Multiplication: 30
print(a / b)    # Division: 3.333...
print(a // b)   # Floor division: 3
print(a % b)    # Modulus (remainder): 1
print(a ** b)   # Exponentiation: 1000
```

### Comparison Operators
```python
x, y = 5, 10

print(x == y)   # Equal: False
print(x != y)   # Not equal: True
print(x < y)    # Less than: True
print(x > y)    # Greater than: False
print(x <= y)   # Less than or equal: True
print(x >= y)   # Greater than or equal: False
```

### Logical Operators
```python
a, b = True, False

print(a and b)  # Logical AND: False
print(a or b)   # Logical OR: True
print(not a)    # Logical NOT: False
```

### Assignment Operators
```python
x = 10
x += 5    # x = x + 5, now x is 15
x -= 3    # x = x - 3, now x is 12
x *= 2    # x = x * 2, now x is 24
x /= 4    # x = x / 4, now x is 6.0
```

---

## Control Structures

### Conditional Statements (if/elif/else)
```python
# Basic if statement
age = 18
if age >= 18:
    print("You are an adult")

# if-else
score = 85
if score >= 60:
    print("You passed!")
else:
    print("You failed!")

# if-elif-else
grade = 92
if grade >= 90:
    print("A grade")
elif grade >= 80:
    print("B grade")
elif grade >= 70:
    print("C grade")
else:
    print("Need improvement")

# Nested conditions
weather = "sunny"
temperature = 75
if weather == "sunny":
    if temperature > 70:
        print("Perfect day for outdoor activities!")
    else:
        print("Sunny but a bit cold")
```

### Loops

#### For Loops
```python
# Loop through a range
for i in range(5):
    print(i)  # Prints 0, 1, 2, 3, 4

# Loop with start, stop, step
for i in range(2, 10, 2):
    print(i)  # Prints 2, 4, 6, 8

# Loop through a string
for char in "Python":
    print(char)  # Prints P, y, t, h, o, n

# Loop through a list
fruits = ["apple", "banana", "orange"]
for fruit in fruits:
    print(f"I like {fruit}")

# Loop with index
for index, fruit in enumerate(fruits):
    print(f"{index}: {fruit}")
```

#### While Loops
```python
# Basic while loop
count = 0
while count < 5:
    print(f"Count: {count}")
    count += 1

# While loop with condition
user_input = ""
while user_input.lower() != "quit":
    user_input = input("Enter 'quit' to exit: ")
    print(f"You entered: {user_input}")
```

#### Loop Control
```python
# break - exit the loop
for i in range(10):
    if i == 5:
        break
    print(i)  # Prints 0, 1, 2, 3, 4

# continue - skip to next iteration
for i in range(10):
    if i % 2 == 0:  # Skip even numbers
        continue
    print(i)  # Prints 1, 3, 5, 7, 9

# else with loops (runs if loop completes normally)
for i in range(3):
    print(i)
else:
    print("Loop completed!")
```

---

## Functions

### Defining Functions
```python
# Basic function
def greet():
    print("Hello!")

greet()  # Call the function

# Function with parameters
def greet_person(name):
    print(f"Hello, {name}!")

greet_person("Alice")

# Function with return value
def add(a, b):
    return a + b

result = add(5, 3)
print(result)  # 8

# Function with default parameters
def greet_with_title(name, title="Mr."):
    return f"Hello, {title} {name}!"

print(greet_with_title("Smith"))           # "Hello, Mr. Smith!"
print(greet_with_title("Johnson", "Dr."))  # "Hello, Dr. Johnson!"
```

### Advanced Function Features
```python
# Multiple return values
def get_name_age():
    return "Alice", 25

name, age = get_name_age()

# Variable arguments (*args)
def sum_all(*numbers):
    return sum(numbers)

print(sum_all(1, 2, 3, 4, 5))  # 15

# Keyword arguments (**kwargs)
def print_info(**info):
    for key, value in info.items():
        print(f"{key}: {value}")

print_info(name="Alice", age=25, city="New York")

# Lambda functions (anonymous functions)
square = lambda x: x ** 2
print(square(5))  # 25

# Lambda with multiple arguments
add = lambda a, b: a + b
print(add(3, 4))  # 7

# Using lambda with built-in functions
numbers = [1, 2, 3, 4, 5]
squared = list(map(lambda x: x**2, numbers))
print(squared)  # [1, 4, 9, 16, 25]
```

---

## Data Structures

### Lists
```python
# Creating lists
fruits = ["apple", "banana", "orange"]
numbers = [1, 2, 3, 4, 5]
mixed = ["hello", 42, True, 3.14]

# List operations
fruits.append("grape")           # Add to end
fruits.insert(1, "kiwi")        # Insert at index 1
fruits.remove("banana")         # Remove by value
popped = fruits.pop()           # Remove and return last item
fruits.extend(["mango", "peach"])  # Add multiple items

# List access and slicing
print(fruits[0])        # First item
print(fruits[-1])       # Last item
print(fruits[1:3])      # Slice: items 1 and 2
print(len(fruits))      # Length of list

# List comprehensions
squares = [x**2 for x in range(10)]
even_squares = [x**2 for x in range(10) if x % 2 == 0]
```

### Tuples
```python
# Creating tuples (immutable)
coordinates = (10, 20)
colors = ("red", "green", "blue")
single_item = (42,)  # Note the comma for single item

# Tuple operations
x, y = coordinates  # Unpacking
print(colors[0])    # Access by index
print(len(colors))  # Length

# Tuples are immutable - this would cause an error:
# colors[0] = "yellow"  # TypeError!
```

### Dictionaries
```python
# Creating dictionaries
person = {
    "name": "Alice",
    "age": 30,
    "city": "New York"
}

# Dictionary operations
person["age"] = 31              # Update value
person["occupation"] = "Engineer"  # Add new key-value pair
del person["city"]              # Delete key-value pair

# Dictionary methods
print(person.keys())            # Get all keys
print(person.values())          # Get all values
print(person.items())           # Get key-value pairs
print(person.get("name"))       # Get value safely
print(person.get("phone", "N/A"))  # Get with default

# Dictionary comprehension
squares_dict = {x: x**2 for x in range(5)}
# {0: 0, 1: 1, 2: 4, 3: 9, 4: 16}
```

### Sets
```python
# Creating sets (unique elements)
fruits = {"apple", "banana", "orange"}
numbers = set([1, 2, 3, 2, 1])  # {1, 2, 3}

# Set operations
fruits.add("grape")
fruits.remove("banana")  # Raises error if not found
fruits.discard("kiwi")   # No error if not found

# Set operations
set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}

print(set1.union(set2))         # {1, 2, 3, 4, 5, 6}
print(set1.intersection(set2))  # {3, 4}
print(set1.difference(set2))    # {1, 2}
```

---

## Object-Oriented Programming

### Classes and Objects
```python
# Basic class definition
class Dog:
    # Class variable
    species = "Canis familiaris"
    
    # Constructor method
    def __init__(self, name, age):
        self.name = name  # Instance variable
        self.age = age
    
    # Instance method
    def bark(self):
        return f"{self.name} says Woof!"
    
    # Method with parameters
    def have_birthday(self):
        self.age += 1
        return f"Happy birthday {self.name}! Now {self.age} years old."

# Creating objects (instances)
dog1 = Dog("Buddy", 3)
dog2 = Dog("Lucy", 5)

print(dog1.bark())  # "Buddy says Woof!"
print(dog1.have_birthday())  # "Happy birthday Buddy! Now 4 years old."
```

### Inheritance
```python
# Parent class
class Animal:
    def __init__(self, name, species):
        self.name = name
        self.species = species
    
    def speak(self):
        return f"{self.name} makes a sound"
    
    def info(self):
        return f"{self.name} is a {self.species}"

# Child class
class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name, "Dog")  # Call parent constructor
        self.breed = breed
    
    def speak(self):  # Override parent method
        return f"{self.name} barks!"
    
    def fetch(self):  # New method specific to Dog
        return f"{self.name} fetches the ball!"

class Cat(Animal):
    def __init__(self, name, indoor=True):
        super().__init__(name, "Cat")
        self.indoor = indoor
    
    def speak(self):
        return f"{self.name} meows!"

# Using inheritance
dog = Dog("Rex", "Golden Retriever")
cat = Cat("Whiskers")

print(dog.speak())  # "Rex barks!"
print(cat.speak())  # "Whiskers meows!"
print(dog.info())   # "Rex is a Dog"
print(dog.fetch())  # "Rex fetches the ball!"
```

### Special Methods (Magic Methods)
```python
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def __str__(self):  # String representation
        return f"Person(name='{self.name}', age={self.age})"
    
    def __repr__(self):  # Developer representation
        return f"Person('{self.name}', {self.age})"
    
    def __eq__(self, other):  # Equality comparison
        if isinstance(other, Person):
            return self.name == other.name and self.age == other.age
        return False
    
    def __lt__(self, other):  # Less than comparison
        return self.age < other.age

person1 = Person("Alice", 25)
person2 = Person("Bob", 30)

print(str(person1))  # Person(name='Alice', age=25)
print(person1 == person2)  # False
print(person1 < person2)   # True
```

---

## File Handling

### Reading Files
```python
# Reading entire file
try:
    with open("example.txt", "r") as file:
        content = file.read()
        print(content)
except FileNotFoundError:
    print("File not found!")

# Reading line by line
with open("example.txt", "r") as file:
    for line in file:
        print(line.strip())  # strip() removes newline characters

# Reading all lines into a list
with open("example.txt", "r") as file:
    lines = file.readlines()
```

### Writing Files
```python
# Writing to a file (overwrites existing content)
with open("output.txt", "w") as file:
    file.write("Hello, World!\n")
    file.write("This is a new line.")

# Appending to a file
with open("output.txt", "a") as file:
    file.write("\nThis line is appended.")

# Writing multiple lines
lines = ["Line 1\n", "Line 2\n", "Line 3\n"]
with open("output.txt", "w") as file:
    file.writelines(lines)
```

### Working with CSV Files
```python
import csv

# Reading CSV
with open("data.csv", "r") as file:
    csv_reader = csv.reader(file)
    for row in csv_reader:
        print(row)

# Writing CSV
data = [
    ["Name", "Age", "City"],
    ["Alice", "25", "New York"],
    ["Bob", "30", "San Francisco"]
]

with open("people.csv", "w", newline="") as file:
    csv_writer = csv.writer(file)
    csv_writer.writerows(data)

# Working with CSV as dictionaries
with open("people.csv", "r") as file:
    csv_reader = csv.DictReader(file)
    for row in csv_reader:
        print(f"{row['Name']} is {row['Age']} years old")
```

---

## Error Handling

### Try-Except Blocks
```python
# Basic exception handling
try:
    number = int(input("Enter a number: "))
    result = 10 / number
    print(f"Result: {result}")
except ValueError:
    print("Invalid input! Please enter a valid number.")
except ZeroDivisionError:
    print("Cannot divide by zero!")

# Catching multiple exceptions
try:
    # Some risky code
    pass
except (ValueError, TypeError) as e:
    print(f"Error occurred: {e}")

# Catching all exceptions
try:
    # Some risky code
    pass
except Exception as e:
    print(f"An error occurred: {e}")

# Finally block (always executes)
try:
    file = open("data.txt", "r")
    # Process file
except FileNotFoundError:
    print("File not found!")
finally:
    # This always runs
    print("Cleanup completed")

# Else block (runs if no exception)
try:
    number = int(input("Enter a number: "))
except ValueError:
    print("Invalid input!")
else:
    print(f"You entered: {number}")
```

### Raising Custom Exceptions
```python
# Raising exceptions
def validate_age(age):
    if age < 0:
        raise ValueError("Age cannot be negative")
    if age > 150:
        raise ValueError("Age seems unrealistic")
    return True

try:
    validate_age(-5)
except ValueError as e:
    print(f"Validation error: {e}")

# Custom exception classes
class CustomError(Exception):
    """A custom exception class"""
    pass

class ValidationError(CustomError):
    """Raised when validation fails"""
    def __init__(self, message, code=None):
        self.message = message
        self.code = code
        super().__init__(self.message)

def validate_email(email):
    if "@" not in email:
        raise ValidationError("Invalid email format", code="INVALID_FORMAT")

try:
    validate_email("invalid-email")
except ValidationError as e:
    print(f"Error: {e.message}, Code: {e.code}")
```

---

## Modules and Packages

### Importing Modules
```python
# Different ways to import
import math
print(math.sqrt(16))  # 4.0

from math import sqrt, pi
print(sqrt(16))  # 4.0
print(pi)        # 3.141592653589793

from math import *  # Import everything (not recommended)
print(cos(0))    # 1.0

import math as m  # Import with alias
print(m.factorial(5))  # 120

from datetime import datetime as dt
now = dt.now()
```

### Creating Your Own Modules
```python
# Save this as calculator.py
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b

# Constants
PI = 3.14159

# This runs only when the module is executed directly
if __name__ == "__main__":
    print("Calculator module loaded")
    print(f"PI = {PI}")

# Using the module (in another file)
# import calculator
# result = calculator.add(5, 3)
# print(result)  # 8
```

### Popular Built-in Modules
```python
# datetime - working with dates and times
from datetime import datetime, timedelta
now = datetime.now()
tomorrow = now + timedelta(days=1)
formatted = now.strftime("%Y-%m-%d %H:%M:%S")

# random - generating random numbers
import random
random_int = random.randint(1, 10)
random_choice = random.choice(["apple", "banana", "orange"])
random.shuffle([1, 2, 3, 4, 5])  # Shuffles in place

# os - operating system interface
import os
current_dir = os.getcwd()
files = os.listdir(".")
os.makedirs("new_directory", exist_ok=True)

# json - working with JSON data
import json
data = {"name": "Alice", "age": 30}
json_string = json.dumps(data)
parsed_data = json.loads(json_string)

# requests - making HTTP requests (needs to be installed)
# pip install requests
# import requests
# response = requests.get("https://api.github.com/users/octocat")
# data = response.json()
```

---

## Advanced Topics

### List Comprehensions and Generators
```python
# List comprehensions
numbers = [1, 2, 3, 4, 5]
squares = [x**2 for x in numbers]
even_squares = [x**2 for x in numbers if x % 2 == 0]

# Nested list comprehensions
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
flattened = [item for row in matrix for item in row]

# Dictionary comprehensions
word_lengths = {word: len(word) for word in ["apple", "banana", "orange"]}

# Set comprehensions
unique_lengths = {len(word) for word in ["apple", "banana", "orange"]}

# Generator expressions (memory efficient)
squares_gen = (x**2 for x in range(1000000))  # Doesn't create all values at once

# Generator functions
def fibonacci():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b

fib = fibonacci()
for i, num in enumerate(fib):
    if i >= 10:
        break
    print(num)
```

### Decorators
```python
# Basic decorator
def my_decorator(func):
    def wrapper():
        print("Something before the function")
        func()
        print("Something after the function")
    return wrapper

@my_decorator
def say_hello():
    print("Hello!")

say_hello()
# Output:
# Something before the function
# Hello!
# Something after the function

# Decorator with arguments
def timer(func):
    import time
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"{func.__name__} took {end - start:.2f} seconds")
        return result
    return wrapper

@timer
def slow_function():
    import time
    time.sleep(1)
    return "Done"

# Decorator with parameters
def repeat(times):
    def decorator(func):
        def wrapper(*args, **kwargs):
            for _ in range(times):
                result = func(*args, **kwargs)
            return result
        return wrapper
    return decorator

@repeat(3)
def greet(name):
    print(f"Hello, {name}!")
```

### Context Managers
```python
# Using context managers
with open("file.txt", "r") as f:
    content = f.read()
# File is automatically closed here

# Creating custom context managers
class MyContextManager:
    def __enter__(self):
        print("Entering context")
        return self
    
    def __exit__(self, exc_type, exc_value, traceback):
        print("Exiting context")
        return False  # Don't suppress exceptions

with MyContextManager() as cm:
    print("Inside context")

# Using contextlib
from contextlib import contextmanager

@contextmanager
def my_context():
    print("Setting up")
    try:
        yield "context value"
    finally:
        print("Cleaning up")

with my_context() as value:
    print(f"Got: {value}")
```

### Regular Expressions
```python
import re

# Basic pattern matching
text = "The price is $25.99"
pattern = r"\$\d+\.\d+"
match = re.search(pattern, text)
if match:
    print(f"Found: {match.group()}")  # Found: $25.99

# Common patterns
email_pattern = r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}"
phone_pattern = r"\d{3}-\d{3}-\d{4}"
url_pattern = r"https?://[^\s]+"

# Using regex functions
text = "Contact us at support@example.com or help@company.org"
emails = re.findall(email_pattern, text)
print(emails)  # ['support@example.com', 'help@company.org']

# Substitution
text = "Hello 123 World 456"
cleaned = re.sub(r"\d+", "[NUMBER]", text)
print(cleaned)  # "Hello [NUMBER] World [NUMBER]"
```

---

## Popular Libraries

### NumPy (Numerical Computing)
```python
import numpy as np

# Creating arrays
arr = np.array([1, 2, 3, 4, 5])
matrix = np.array([[1, 2], [3, 4]])
zeros = np.zeros((3, 3))
ones = np.ones((2, 4))
random_arr = np.random.random((3, 3))

# Array operations
arr2 = arr * 2  # Element-wise multiplication
arr_sum = np.sum(arr)
arr_mean = np.mean(arr)
arr_max = np.max(arr)

# Linear algebra
a = np.array([[1, 2], [3, 4]])
b = np.array([[5, 6], [7, 8]])
matrix_mult = np.dot(a, b)
```

### Pandas (Data Analysis)
```python
import pandas as pd

# Creating DataFrames
data = {
    'Name': ['Alice', 'Bob', 'Charlie'],
    'Age': [25, 30, 35],
    'Salary': [50000, 60000, 70000]
}
df = pd.DataFrame(data)

# Reading from files
# df = pd.read_csv('data.csv')
# df = pd.read_excel('data.xlsx')

# Basic operations
print(df.head())  # First 5 rows
print(df.info())  # DataFrame info
print(df.describe())  # Statistical summary

# Filtering and selection
young_people = df[df['Age'] < 30]
names_ages = df[['Name', 'Age']]

# Grouping and aggregation
avg_salary_by_age = df.groupby('Age')['Salary'].mean()
```

### Matplotlib (Plotting)
```python
import matplotlib.pyplot as plt

# Basic plot
x = [1, 2, 3, 4, 5]
y = [2, 4, 6, 8, 10]
plt.plot(x, y)
plt.xlabel('X values')
plt.ylabel('Y values')
plt.title('Simple Line Plot')
plt.show()

# Multiple plot types
fig, axes = plt.subplots(2, 2, figsize=(10, 8))

# Line plot
axes[0, 0].plot(x, y)
axes[0, 0].set_title('Line Plot')

# Bar plot
axes[0, 1].bar(['A', 'B', 'C'], [1, 3, 2])
axes[0, 1].set_title('Bar Plot')

# Histogram
data = np.random.normal(0, 1, 1000)
axes[1, 0].hist(data, bins=30)
axes[1, 0].set_title('Histogram')

# Scatter plot
x_scatter = np.random.randn(100)
y_scatter = np.random.randn(100)
axes[1, 1].scatter(x_scatter, y_scatter)
axes[1, 1].set_title('Scatter Plot')

plt.tight_layout()
plt.show()
```

---

## Practice Projects

### Project 1: Todo List Manager
```python
class TodoList:
    def __init__(self):
        self.tasks = []
    
    def add_task(self, task):
        self.tasks.append({"task": task, "completed": False})
        print(f"Added: {task}")
    
    def complete_task(self, index):
        if 0 <= index < len(self.tasks):
            self.tasks[index]["completed"] = True
            print(f"Completed: {self.tasks[index]['task']}")
        else:
            print("Invalid task index")
    
    def show_tasks(self):
        if not self.tasks:
            print("No tasks!")
            return
        
        for i, task in enumerate(self.tasks):
            status = "✓" if task["completed"] else "○"
            print(f"{i + 1}. {status} {task['task']}")
    
    def remove_task(self, index):
        if 0 <= index < len(self.tasks):
            removed = self.tasks.pop(index)
            print(f"Removed: {removed['task']}")
        else:
            print("Invalid task index")

# Usage
todo = TodoList()
todo.add_task("Learn Python")
todo.add_task("Build a project")
todo.show_tasks()
todo.complete_task(0)
todo.show_tasks()
```

### Project 2: Simple Calculator
```python
class Calculator:
    def __init__(self):
        self.history = []
    
    def add(self, a, b):
        result = a + b
        self.history.append(f"{a} + {b} = {result}")
        return result
    
    def subtract(self, a, b):
        result = a - b
        self.history.append(f"{a} - {b} = {result}")
        return result
    
    def multiply(self, a, b):
        result = a * b
        self.history.append(f"{a} * {b} = {result}")
        return result
    
    def divide(self, a, b):
        if b == 0:
            raise ValueError("Cannot divide by zero")
        result = a / b
        self.history.append(f"{a} / {b} = {result}")
        return result
    
    def show_history(self):
        if not self.history:
            print("No calculations yet")
            return
        
        print("Calculation History:")
        for calc in self.history:
            print(f"  {calc}")

def main():
    calc = Calculator()
    
    while True:
        print("\n=== Calculator ===")
        print("1. Add")
        print("2. Subtract")
        print("3. Multiply")
        print("4. Divide")
        print("5. Show History")
        print("6. Quit")
        
        choice = input("Choose an option: ")
        
        if choice == "6":
            break
        elif choice == "5":
            calc.show_history()
            continue
        
        try:
            a = float(input("Enter first number: "))
            b = float(input("Enter second number: "))
            
            if choice == "1":
                result = calc.add(a, b)
            elif choice == "2":
                result = calc.subtract(a, b)
            elif choice == "3":
                result = calc.multiply(a, b)
            elif choice == "4":
                result = calc.divide(a, b)
            else:
                print("Invalid choice")
                continue
            
            print(f"Result: {result}")
            
        except ValueError as e:
            print(f"Error: {e}")
        except Exception as e:
            print(f"Unexpected error: {e}")

if __name__ == "__main__":
    main()
```

### Project 3: Password Generator
```python
import random
import string

class PasswordGenerator:
    def __init__(self):
        self.lowercase = string.ascii_lowercase
        self.uppercase = string.ascii_uppercase
        self.digits = string.digits
        self.symbols = "!@#$%^&*"
    
    def generate_password(self, length=12, use_uppercase=True, 
                         use_digits=True, use_symbols=True):
        if length < 4:
            raise ValueError("Password length should be at least 4")
        
        # Start with lowercase letters
        chars = self.lowercase
        password = [random.choice(self.lowercase)]
        
        # Add character sets based on options
        if use_uppercase:
            chars += self.uppercase
            password.append(random.choice(self.uppercase))
        
        if use_digits:
            chars += self.digits
            password.append(random.choice(self.digits))
        
        if use_symbols:
            chars += self.symbols
            password.append(random.choice(self.symbols))
        
        # Fill the rest with random characters
        for _ in range(length - len(password)):
            password.append(random.choice(chars))
        
        # Shuffle the password list
        random.shuffle(password)
        
        return ''.join(password)
    
    def check_strength(self, password):
        score = 0
        feedback = []
        
        if len(password) >= 8:
            score += 1
        else:
            feedback.append("Use at least 8 characters")
        
        if any(c.islower() for c in password):
            score += 1
        else:
            feedback.append("Add lowercase letters")
        
        if any(c.isupper() for c in password):
            score += 1
        else:
            feedback.append("Add uppercase letters")
        
        if any(c.isdigit() for c in password):
            score += 1
        else:
            feedback.append("Add numbers")
        
        if any(c in self.symbols for c in password):
            score += 1
        else:
            feedback.append("Add symbols")
        
        strength_levels = ["Very Weak", "Weak", "Fair", "Good", "Strong"]
        strength = strength_levels[min(score, 4)]
        
        return {
            "strength": strength,
            "score": score,
            "feedback": feedback
        }

# Usage
generator = PasswordGenerator()
password = generator.generate_password(length=16)
print(f"Generated password: {password}")

strength_info = generator.check_strength(password)
print(f"Strength: {strength_info['strength']}")
```

---

## Best Practices

### Code Style (PEP 8)
```python
# Good naming conventions
user_name = "Alice"  # snake_case for variables and functions
USER_COUNT = 100     # UPPER_CASE for constants

class UserManager:   # PascalCase for classes
    pass

def calculate_total_price():  # Descriptive function names
    pass

# Proper spacing
def example_function(param1, param2, param3=None):
    if param3 is None:
        param3 = []
    
    result = param1 + param2
    return result

# Good comments
def fibonacci(n):
    """
    Generate the nth Fibonacci number.
    
    Args:
        n (int): The position in the Fibonacci sequence
        
    Returns:
        int: The nth Fibonacci number
        
    Raises:
        ValueError: If n is negative
    """
    if n < 0:
        raise ValueError("n must be non-negative")
    
    if n <= 1:
        return n
    
    # Use iterative approach for efficiency
    a, b = 0, 1
    for _ in range(2, n + 1):
        a, b = b, a + b
    
    return b
```

### Error Handling Best Practices
```python
# Be specific with exceptions
def divide_numbers(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        print("Cannot divide by zero")
        return None
    except TypeError:
        print("Both arguments must be numbers")
        return None

# Use context managers for resources
def read_config_file(filename):
    try:
        with open(filename, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        print(f"Config file {filename} not found")
        return {}
    except json.JSONDecodeError:
        print(f"Invalid JSON in {filename}")
        return {}

# Validate input early
def calculate_age(birth_year):
    current_year = datetime.now().year
    
    if not isinstance(birth_year, int):
        raise TypeError("Birth year must be an integer")
    
    if birth_year > current_year:
        raise ValueError("Birth year cannot be in the future")
    
    if birth_year < 1900:
        raise ValueError("Birth year seems unrealistic")
    
    return current_year - birth_year
```

### Performance Tips
```python
# Use list comprehensions instead of loops when possible
# Slow
squares = []
for i in range(1000):
    squares.append(i ** 2)

# Fast
squares = [i ** 2 for i in range(1000)]

# Use generators for large datasets
def large_fibonacci():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b

# Use built-in functions
numbers = [1, 2, 3, 4, 5]
total = sum(numbers)  # Better than manual loop
maximum = max(numbers)
minimum = min(numbers)

# Use sets for membership testing
large_list = list(range(10000))
large_set = set(large_list)

# Slow
if 5000 in large_list:  # O(n)
    pass

# Fast
if 5000 in large_set:   # O(1)
    pass
```

### Testing Your Code
```python
import unittest

def add_numbers(a, b):
    """Add two numbers together."""
    return a + b

def divide_numbers(a, b):
    """Divide a by b."""
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b

class TestMathFunctions(unittest.TestCase):
    
    def test_add_numbers(self):
        self.assertEqual(add_numbers(2, 3), 5)
        self.assertEqual(add_numbers(-1, 1), 0)
        self.assertEqual(add_numbers(0, 0), 0)
    
    def test_divide_numbers(self):
        self.assertEqual(divide_numbers(10, 2), 5)
        self.assertEqual(divide_numbers(7, 2), 3.5)
        
        # Test exception
        with self.assertRaises(ValueError):
            divide_numbers(10, 0)

if __name__ == "__main__":
    unittest.main()
```

---

## Next Steps and Resources

### Intermediate Topics to Explore
1. **Web Development**: Learn Flask or Django
2. **Data Science**: Dive deeper into NumPy, Pandas, Matplotlib, Seaborn
3. **Machine Learning**: Explore scikit-learn, TensorFlow, PyTorch
4. **Web Scraping**: BeautifulSoup, Scrapy, Selenium
5. **API Development**: FastAPI, REST APIs
6. **Database Integration**: SQLAlchemy, Django ORM
7. **Testing**: pytest, unittest, test-driven development
8. **Async Programming**: asyncio, async/await

### Recommended Practice
1. **Daily Coding**: Solve problems on platforms like:
   - LeetCode
   - HackerRank
   - Codewars
   - Python Challenge

2. **Build Projects**: Start with simple projects and gradually increase complexity:
   - Command-line tools
   - Web applications
   - Data analysis projects
   - Automation scripts

3. **Read Code**: Study well-written Python code on GitHub

4. **Join Communities**:
   - Reddit: r/Python, r/learnpython
   - Stack Overflow
   - Python Discord servers
   - Local Python meetups

### Essential Tools and Libraries
```python
# Development tools
pip install black      # Code formatter
pip install flake8     # Linter
pip install mypy       # Type checker
pip install pytest     # Testing framework

# Popular libraries
pip install requests   # HTTP library
pip install pandas     # Data analysis
pip install numpy      # Numerical computing
pip install matplotlib # Plotting
pip install flask      # Web framework
pip install beautifulsoup4  # Web scraping
```

---

## Conclusion

Congratulations! You now have a comprehensive foundation in Python programming. Remember:

1. **Practice Regularly**: Coding is a skill that improves with practice
2. **Build Projects**: Apply what you learn to real-world problems
3. **Read Documentation**: Get comfortable reading Python docs and library documentation
4. **Debug Systematically**: Learn to read error messages and use debugging tools
5. **Stay Updated**: Python evolves, so keep learning new features and best practices

Start with the basics, practice consistently, and gradually move to more advanced topics. Most importantly, have fun coding! 🐍✨

---

*Happy Python Programming!* 🎉