"""
📁 11_ModulesPackages/module_usage.py
🧠 Topic: Python Modules and Packages (Import Systems)

Key Concepts Covered:
1. Importing standard libraries (math, os, sys, datetime)
2. Importing custom modules (from my_math)
3. Aliasing (import ... as ...)
4. Selective importing (from ... import ...)
5. The '__name__' variable and its role.

Interview Focus:
- Difference between 'import math' and 'from math import *'? (Namespace pollution)
- What is a Python package? (Folder with __init__.py)
- Purpose of '__init__.py'? (Identifies a folder as a package/package initialization)
- How to check where Python searches for modules? (sys.path)
"""

# Standard Libraries
import os
import sys
import datetime
import math # used via math.sqrt etc.

# Custom Local Module (Must be in the same folder or path)
try:
    import my_math
    # from my_math import add, subtract
except ImportError:
    print("⚠️ my_math.py NOT found. Ensure both files are in same directory.")

def demonstrate_standard_libs():
    """Exploring powerful built-in Python tools."""
    print("\n--- Standard Library Examples ---")
    
    # math
    print(f"PI from math lib: {math.pi}")
    print(f"Square root of 16: {math.sqrt(16)}")
    
    # datetime
    now = datetime.datetime.now()
    print(f"Current Date/Time: {now.strftime('%Y-%m-%d %H:%M:%S')}")
    
    # os (operating system)
    print(f"Current Working Directory: {os.getcwd()}")
    
    # sys
    print(f"Platform: {sys.platform}")
    print(f"Python sys.path entry count: {len(sys.path)}")

def demonstrate_custom_imports():
    """Importing logic from our own files."""
    print("\n--- Custom Module Imports (my_math.py) ---")
    
    # 1. Accessing variables directly from aliased/imported module
    print(f"my_math.PI: {my_math.PI}")
    
    # 2. Accessing functions
    res_add = my_math.add(10, 20)
    res_sub = my_math.subtract(100, 50)
    print(f"my_math.add(10, 20): {res_add}")
    print(f"my_math.subtract(100, 50): {res_sub}")

def explain_aliasing():
    """Using short aliases for long module names."""
    print("\n--- Selective Importing and Aliasing ---")
    
    # import datetime as dt
    # from math import sqrt as r
    
    from math import factorial as fact
    print(f"5! using alias 'fact': {fact(5)}")

def package_structure_intro():
    """Quick explanation of Python Packages vs Modules."""
    print("\n--- Packages vs Modules ---")
    
    print("1. Module: A single .py file.")
    print("2. Package: A folder containing multiple .py files AND an '__init__.py' file.")
    print("Summary: Packages help in organizing large codebases into hierarchical structures.")

def main():
    print("🚀 Python Modules and Packages Practice")
    demonstrate_standard_libs()
    demonstrate_custom_imports()
    explain_aliasing()
    package_structure_intro()

if __name__ == "__main__":
    main()

"""
Input/Output Examples:
Output:
PI from math lib: 3.141592653589793
...
my_math.PI: 3.14159265
...
Current Working Directory: d:\\Python\\11_ModulesPackages
...
"""
