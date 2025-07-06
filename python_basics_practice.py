#!/usr/bin/env python3
"""
Python Basics Practice File
Run this file to see examples and practice basic Python concepts.
"""

def main():
    print("=" * 50)
    print("PYTHON BASICS PRACTICE")
    print("=" * 50)
    
    # 1. Variables and Data Types
    print("\n1. VARIABLES AND DATA TYPES")
    print("-" * 30)
    
    name = "Alice"
    age = 25
    height = 5.6
    is_student = True
    
    print(f"Name: {name} (type: {type(name).__name__})")
    print(f"Age: {age} (type: {type(age).__name__})")
    print(f"Height: {height} (type: {type(height).__name__})")
    print(f"Is Student: {is_student} (type: {type(is_student).__name__})")
    
    # 2. String Operations
    print("\n2. STRING OPERATIONS")
    print("-" * 30)
    
    text = "  Hello Python World  "
    print(f"Original: '{text}'")
    print(f"Stripped: '{text.strip()}'")
    print(f"Uppercase: '{text.upper()}'")
    print(f"Lowercase: '{text.lower()}'")
    print(f"Replace 'Python' with 'Amazing': '{text.replace('Python', 'Amazing')}'")
    print(f"Length: {len(text)}")
    
    # String slicing
    word = "Python"
    print(f"\nString slicing with '{word}':")
    print(f"First character: {word[0]}")
    print(f"Last character: {word[-1]}")
    print(f"First 3 characters: {word[:3]}")
    print(f"Last 3 characters: {word[-3:]}")
    print(f"Middle (1:4): {word[1:4]}")
    
    # 3. Lists
    print("\n3. LISTS")
    print("-" * 30)
    
    fruits = ["apple", "banana", "orange"]
    print(f"Original list: {fruits}")
    
    fruits.append("grape")
    print(f"After append: {fruits}")
    
    fruits.insert(1, "kiwi")
    print(f"After insert at index 1: {fruits}")
    
    removed = fruits.pop()
    print(f"After pop: {fruits} (removed: {removed})")
    
    # List comprehension
    numbers = [1, 2, 3, 4, 5]
    squares = [x**2 for x in numbers]
    print(f"Numbers: {numbers}")
    print(f"Squares: {squares}")
    
    # 4. Dictionaries
    print("\n4. DICTIONARIES")
    print("-" * 30)
    
    person = {
        "name": "Bob",
        "age": 30,
        "city": "New York"
    }
    
    print(f"Person: {person}")
    print(f"Name: {person['name']}")
    print(f"Age: {person.get('age', 'Unknown')}")
    
    person["occupation"] = "Engineer"
    print(f"After adding occupation: {person}")
    
    print(f"Keys: {list(person.keys())}")
    print(f"Values: {list(person.values())}")
    
    # 5. Control Structures
    print("\n5. CONTROL STRUCTURES")
    print("-" * 30)
    
    # If statements
    score = 85
    if score >= 90:
        grade = "A"
    elif score >= 80:
        grade = "B"
    elif score >= 70:
        grade = "C"
    else:
        grade = "F"
    
    print(f"Score: {score}, Grade: {grade}")
    
    # Loops
    print("\nFor loop with range:")
    for i in range(5):
        print(f"  {i}: {i**2}")
    
    print("\nFor loop with list:")
    colors = ["red", "green", "blue"]
    for i, color in enumerate(colors):
        print(f"  {i}: {color}")
    
    # 6. Functions
    print("\n6. FUNCTIONS")
    print("-" * 30)
    
    def greet(name, greeting="Hello"):
        return f"{greeting}, {name}!"
    
    def calculate_area(length, width):
        return length * width
    
    print(greet("Alice"))
    print(greet("Bob", "Hi"))
    print(f"Area of 5x3 rectangle: {calculate_area(5, 3)}")
    
    # 7. Error Handling
    print("\n7. ERROR HANDLING")
    print("-" * 30)
    
    def safe_divide(a, b):
        try:
            result = a / b
            return f"{a} / {b} = {result}"
        except ZeroDivisionError:
            return "Error: Cannot divide by zero!"
        except TypeError:
            return "Error: Both arguments must be numbers!"
    
    print(safe_divide(10, 2))
    print(safe_divide(10, 0))
    print(safe_divide("10", 2))
    
    print("\n" + "=" * 50)
    print("Practice completed! Try modifying the values above.")
    print("=" * 50)

if __name__ == "__main__":
    main()