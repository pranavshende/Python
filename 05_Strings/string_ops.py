"""
📁 05_Strings/string_ops.py
🧠 Topic: String Operations, Slicing, and Formatting

Key Concepts Covered:
1. String Creation (Single, Double, Triple Quotes)
2. String Immutability (Strings cannot be modified in place)
3. String Concatenation and Repetition
4. String Slicing [start:stop:step]
5. Formatted Strings (f-strings, .format(), %-operator)

Interview Focus:
- Why are strings immutable in Python? (Memory safety, caching, performance)
- How to reverse a string in ONE line? [::-1]
- Formatting complex expressions in f-strings.
"""

def string_basics():
    """Basics of string declaration and behavior."""
    print("\n--- String Declaration and Immutability ---")
    
    # 1. Declaration styles
    single = 'Single quote string'
    double = "Double quote string"
    triple = \"\"\"Triple quote string
    can span multiple lines.\"\"\"
    
    print(f"Created strings: {single}, {double}")
    print(f"Triple quoted: {triple.strip()}")
    
    # 2. Immutability (Strings are fixed once created)
    text = "Hello"
    try:
        # text[0] = 'h' # Raising TypeError manually for demo
        print(f"Original text: {text}")
        print("Verification: Cannot assign new characters directly (text[0] = 'h' will FAIL).")
    except TypeError as e:
        print(f"Caught ERROR: {e}")

def string_operations():
    """Operations using operators like +, *, and comparison."""
    print("\n--- Arithmetic String Operations ---")
    
    # Concatenation (+)
    first = "Hello"
    second = "Python"
    print(f"Concatenation: {first + ' ' + second}")
    
    # Repetition (*)
    print(f"Repetition: 'Hi! ' * 3 = {'Hi! ' * 3}")
    
    # Length of string
    print(f"Length: len('{first}') = {len(first)}")

def slicing_patterns():
    """Extracting sub-strings using indices and steps."""
    print("\n--- String Slicing (start:stop:step) ---")
    
    # Positive Index: 0 to N-1
    # Negative Index: -N to -1
    
    msg = "Python Programming"
    
    # msg[0:6] -> index 0 to 5
    print(f"msg[0:6]: '{msg[0:6]}'")
    
    # Step: Every 2nd character
    print(f"msg[::2]: '{msg[::2]}'")
    
    # Reverse a string using negative step (Interview Question)
    print(f"Reversed msg[::-1]: '{msg[::-1]}'")
    
    # Skip first 7 characters
    print(f"msg[7:]: '{msg[7:]}'")

def advanced_formatting():
    """Modern ways of handling dynamic strings."""
    print("\n--- Advanced string formatting ---")
    
    name, age = "Alice", 25
    
    # 1. F-Strings (Preferred: Python 3.6+)
    print(f"F-String: Hello, I'm {name} and I am {age} years old.")
    
    # 2. .format() method (Old school but flexible)
    print("Format Method: My name is {0} and I'm {1}.".format(name, age))
    
    # 3. Formatting numbers
    pi = 3.14159265
    print(f"Formatting PI to 2 decimal places: {pi:.2f}")

def main():
    print("🚀 Python String Operations and Formatting Practice")
    string_basics()
    string_operations()
    slicing_patterns()
    advanced_formatting()

if __name__ == "__main__":
    main()

"""
Input/Output Examples:
Output:
Verification: Cannot assign new characters directly ...
Concatenation: Hello Python
...
msg[0:6]: 'Python'
Reversed msg[::-1]: 'gnimmargorP nohtyP'
...
Formatting PI to 2 decimal places: 3.14
"""
