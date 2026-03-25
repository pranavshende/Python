"""
📁 01_Basics/variables_data_types.py
🧠 Topic: Variables and Data Types

Key Concepts Covered:
1. Dynamic Typing (no explicit type declaration)
2. Fundamental Data Types (int, float, complex, bool, str)
3. Type Checking (type() and isinstance())
4. Identifying Unique Objects (id())

Interview Focus:
- How does Python differ from static typed languages (e.g., Java)?
- What's the difference between int and float behavior?
- Python's memory management: How are variables stored?
"""

import sys

def explain_variable_assignment():
    """Shows how variables are assigned and reassigned in Python."""
    print("\n--- Variable Assignment ---")
    
    # Python is dynamically typed
    count = 10        # int
    price = 19.99     # float
    is_valid = True    # bool
    name = "Python"    # str
    
    print(f"Initial variables: count={count}, price={price}, is_valid={is_valid}, name={name}")
    
    # Reassigning to different type (legal in Python)
    count = "Now I am a string"
    print(f"Reassigned count: {count} (Now type is {type(count)})")

def explore_data_types():
    """Details fundamental data types and their properties."""
    print("\n--- Exploring Data Types ---")
    
    # 1. Numeric
    i = 42
    f = 42.0
    c = 3 + 4j  # Complex: Real part=3, Imaginary part=4
    
    # 2. Boolean
    is_true = True
    is_false = False
    
    # 3. String
    s = "Hello World"
    
    # 4. None Type (Special type for void/null)
    n = None
    
    data = [i, f, c, is_true, is_false, s, n]
    
    for item in data:
        print(f"Value: {item:12} | Type: {type(item).__name__:10} | id: {id(item)}")

def check_type_safety():
    """Demonstrates type identification using isinstance()."""
    print("\n--- Type Checking with isinstance() ---")
    
    value = 3.14159
    
    if isinstance(value, float):
        print(f"{value} is definitely a float.")
    
    if isinstance(value, (int, float)):
        print(f"{value} is a numeric type (int or float).")

def solve_edge_cases():
    """Addresses tricky scenarios like overflows and precision."""
    print("\n--- Edge Cases & Interview Questions ---")
    
    # 1. Floating point precision issue (classic interview question)
    calc = 0.1 + 0.2
    print(f"0.1 + 0.2 equals {calc}")
    print(f"Is 0.1 + 0.2 == 0.3? {calc == 0.3}")
    
    # 2. Large integers (Python handles arbitrarily large integers)
    large_num = 10**100
    print(f"Large number (10^100) length: {len(str(large_num))}")
    
    # 3. Boolean in math (Booleans are subclasses of int: True=1, False=0)
    bool_sum = True + True + False 
    print(f"True + True + False = {bool_sum}")

def main():
    print("🚀 Python Variables and Data Types Practice")
    explain_variable_assignment()
    explore_data_types()
    check_type_safety()
    solve_edge_cases()

if __name__ == "__main__":
    main()

"""
Input/Output Examples:
Output:
🚀 Python Variables and Data Types Practice
--- Variable Assignment ---
Initial variables: count=10, price=19.99, is_valid=True, name=Python
Reassigned count: Now I am a string (Now type is <class 'str'>)
...
--- Edge Cases & Interview Questions ---
0.1 + 0.2 equals 0.30000000000000004
Is 0.1 + 0.2 == 0.3? False
Large number (10^100) length: 101
True + True + False = 2
"""
