#!/usr/bin/env python3
"""
Python Practice Exercises
Complete each exercise by implementing the requested function.
Test your solutions by running this file.
"""

def exercise_1():
    """
    Exercise 1: FizzBuzz
    Write a function that prints numbers 1 to 100, but:
    - For multiples of 3, print "Fizz" instead
    - For multiples of 5, print "Buzz" instead  
    - For multiples of both 3 and 5, print "FizzBuzz"
    """
    print("Exercise 1: FizzBuzz")
    print("-" * 20)
    
    # TODO: Implement your solution here
    def fizzbuzz():
        for i in range(1, 101):
            if i % 15 == 0:
                print("FizzBuzz")
            elif i % 3 == 0:
                print("Fizz")
            elif i % 5 == 0:
                print("Buzz")
            else:
                print(i)
    
    # Test your function
    # fizzbuzz()  # Uncomment to see output
    print("FizzBuzz function implemented!")

def exercise_2():
    """
    Exercise 2: Palindrome Checker
    Write a function that checks if a string is a palindrome
    (reads the same forwards and backwards)
    """
    print("\nExercise 2: Palindrome Checker")
    print("-" * 30)
    
    def is_palindrome(text):
        # TODO: Implement your solution here
        # Hint: Consider case sensitivity and spaces
        cleaned = text.lower().replace(" ", "")
        return cleaned == cleaned[::-1]
    
    # Test cases
    test_cases = ["racecar", "hello", "A man a plan a canal Panama", "race a car"]
    for case in test_cases:
        result = is_palindrome(case)
        print(f"'{case}' is palindrome: {result}")

def exercise_3():
    """
    Exercise 3: List Statistics
    Write functions to calculate basic statistics from a list of numbers
    """
    print("\nExercise 3: List Statistics")
    print("-" * 25)
    
    def calculate_stats(numbers):
        # TODO: Implement your solution here
        if not numbers:
            return None
        
        total = sum(numbers)
        count = len(numbers)
        average = total / count
        minimum = min(numbers)
        maximum = max(numbers)
        
        return {
            "sum": total,
            "count": count,
            "average": average,
            "min": minimum,
            "max": maximum
        }
    
    # Test with sample data
    test_numbers = [1, 5, 3, 9, 2, 8, 4, 7, 6]
    stats = calculate_stats(test_numbers)
    print(f"Numbers: {test_numbers}")
    for key, value in stats.items():
        print(f"{key.capitalize()}: {value}")

def exercise_4():
    """
    Exercise 4: Word Counter
    Write a function that counts the frequency of each word in a text
    """
    print("\nExercise 4: Word Counter")
    print("-" * 20)
    
    def count_words(text):
        # TODO: Implement your solution here
        # Hint: Consider punctuation and case sensitivity
        import string
        
        # Remove punctuation and convert to lowercase
        translator = str.maketrans("", "", string.punctuation)
        cleaned_text = text.translate(translator).lower()
        
        words = cleaned_text.split()
        word_count = {}
        
        for word in words:
            word_count[word] = word_count.get(word, 0) + 1
        
        return word_count
    
    # Test with sample text
    sample_text = "The quick brown fox jumps over the lazy dog. The dog was really lazy!"
    word_counts = count_words(sample_text)
    print(f"Text: {sample_text}")
    print("Word frequencies:")
    for word, count in sorted(word_counts.items()):
        print(f"  {word}: {count}")

def exercise_5():
    """
    Exercise 5: Number Guessing Game
    Create a simple number guessing game
    """
    print("\nExercise 5: Number Guessing Game")
    print("-" * 30)
    
    def number_guessing_game():
        import random
        
        # TODO: Implement your solution here
        target = random.randint(1, 100)
        attempts = 0
        max_attempts = 7
        
        print("I'm thinking of a number between 1 and 100!")
        print(f"You have {max_attempts} attempts to guess it.")
        
        while attempts < max_attempts:
            try:
                guess = int(input("Enter your guess: "))
                attempts += 1
                
                if guess == target:
                    print(f"Congratulations! You guessed it in {attempts} attempts!")
                    break
                elif guess < target:
                    print("Too low!")
                else:
                    print("Too high!")
                
                remaining = max_attempts - attempts
                if remaining > 0:
                    print(f"You have {remaining} attempts left.")
                else:
                    print(f"Game over! The number was {target}")
                    
            except ValueError:
                print("Please enter a valid number!")
    
    # Uncomment to play the game
    # number_guessing_game()
    print("Number guessing game implemented!")

def exercise_6():
    """
    Exercise 6: Simple Calculator Class
    Create a calculator class with basic operations and history
    """
    print("\nExercise 6: Simple Calculator Class")
    print("-" * 35)
    
    class Calculator:
        def __init__(self):
            # TODO: Initialize the calculator
            self.history = []
        
        def add(self, a, b):
            # TODO: Implement addition
            result = a + b
            self.history.append(f"{a} + {b} = {result}")
            return result
        
        def subtract(self, a, b):
            # TODO: Implement subtraction
            result = a - b
            self.history.append(f"{a} - {b} = {result}")
            return result
        
        def multiply(self, a, b):
            # TODO: Implement multiplication
            result = a * b
            self.history.append(f"{a} * {b} = {result}")
            return result
        
        def divide(self, a, b):
            # TODO: Implement division with error handling
            if b == 0:
                raise ValueError("Cannot divide by zero")
            result = a / b
            self.history.append(f"{a} / {b} = {result}")
            return result
        
        def get_history(self):
            # TODO: Return calculation history
            return self.history.copy()
        
        def clear_history(self):
            # TODO: Clear calculation history
            self.history.clear()
    
    # Test the calculator
    calc = Calculator()
    print(f"10 + 5 = {calc.add(10, 5)}")
    print(f"20 - 8 = {calc.subtract(20, 8)}")
    print(f"6 * 7 = {calc.multiply(6, 7)}")
    print(f"15 / 3 = {calc.divide(15, 3)}")
    
    print("\nCalculation History:")
    for calculation in calc.get_history():
        print(f"  {calculation}")

def exercise_7():
    """
    Exercise 7: File Operations
    Practice reading and writing files
    """
    print("\nExercise 7: File Operations")
    print("-" * 25)
    
    def create_sample_file():
        # TODO: Create a sample text file with some data
        sample_data = [
            "Python is awesome!",
            "Learning programming is fun.",
            "Practice makes perfect.",
            "Keep coding!",
            "Don't give up!"
        ]
        
        with open("sample.txt", "w") as file:
            for line in sample_data:
                file.write(line + "\n")
        
        print("Created sample.txt")
    
    def read_and_analyze_file(filename):
        # TODO: Read file and return analysis
        try:
            with open(filename, "r") as file:
                lines = file.readlines()
            
            total_lines = len(lines)
            total_words = sum(len(line.split()) for line in lines)
            total_chars = sum(len(line) for line in lines)
            
            return {
                "lines": total_lines,
                "words": total_words,
                "characters": total_chars
            }
        except FileNotFoundError:
            return None
    
    # Test file operations
    create_sample_file()
    analysis = read_and_analyze_file("sample.txt")
    
    if analysis:
        print(f"File analysis:")
        print(f"  Lines: {analysis['lines']}")
        print(f"  Words: {analysis['words']}")
        print(f"  Characters: {analysis['characters']}")

def exercise_8():
    """
    Exercise 8: List Manipulation
    Practice advanced list operations
    """
    print("\nExercise 8: List Manipulation")
    print("-" * 27)
    
    def remove_duplicates(lst):
        # TODO: Remove duplicates while preserving order
        seen = set()
        result = []
        for item in lst:
            if item not in seen:
                seen.add(item)
                result.append(item)
        return result
    
    def find_common_elements(list1, list2):
        # TODO: Find elements common to both lists
        return list(set(list1) & set(list2))
    
    def merge_sorted_lists(list1, list2):
        # TODO: Merge two sorted lists into one sorted list
        result = []
        i = j = 0
        
        while i < len(list1) and j < len(list2):
            if list1[i] <= list2[j]:
                result.append(list1[i])
                i += 1
            else:
                result.append(list2[j])
                j += 1
        
        # Add remaining elements
        result.extend(list1[i:])
        result.extend(list2[j:])
        
        return result
    
    # Test the functions
    test_list = [1, 2, 3, 2, 4, 1, 5]
    print(f"Original: {test_list}")
    print(f"Remove duplicates: {remove_duplicates(test_list)}")
    
    list_a = [1, 2, 3, 4, 5]
    list_b = [4, 5, 6, 7, 8]
    print(f"List A: {list_a}")
    print(f"List B: {list_b}")
    print(f"Common elements: {find_common_elements(list_a, list_b)}")
    
    sorted_a = [1, 3, 5, 7]
    sorted_b = [2, 4, 6, 8]
    print(f"Sorted A: {sorted_a}")
    print(f"Sorted B: {sorted_b}")
    print(f"Merged: {merge_sorted_lists(sorted_a, sorted_b)}")

def main():
    """Run all exercises"""
    print("PYTHON PRACTICE EXERCISES")
    print("=" * 50)
    
    exercises = [
        exercise_1,
        exercise_2,
        exercise_3,
        exercise_4,
        exercise_5,
        exercise_6,
        exercise_7,
        exercise_8
    ]
    
    for exercise in exercises:
        try:
            exercise()
        except Exception as e:
            print(f"Error in exercise: {e}")
    
    print("\n" + "=" * 50)
    print("All exercises completed!")
    print("Try modifying the solutions to explore different approaches.")
    print("=" * 50)

if __name__ == "__main__":
    main()