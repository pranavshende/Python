"""
📁 11_ModulesPackages/my_math.py
🧠 A sample module to demonstrate Python's custom import systems.
"""

# 1. Variables in a module
PI = 3.14159265
GOLDEN_RATIO = 1.618

# 2. Functions in a module
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

# 3. Private-like variables (by convention)
_internal_data = "Hidden from general import *"

# 4. Main block inside module (not executed when imported)
if __name__ == "__main__":
    print("This runs only if YOU execute my_math.py directly!")
    print(f"Sum of 5 + 5: {add(5, 5)}")
