"""
📁 01_Basics/basics.py
🧠 Topic: Python Basics (Syntax, Indentation, and Structure)

Key Concepts Covered:
1. Python Syntax & Indentation
2. Documenting Code (Comments & Docstrings)
3. Python Script Structure (Main block)
4. Case Sensitivity

Interview Focus:
- Why is indentation critical in Python?
- Difference between single-line and multi-line comments.
- Purpose of `if __name__ == "__main__":`
"""

import sys

def explain_indentation():
    """Demonstrates how Python uses indentation to define code blocks."""
    print("\n--- Indentation in Python ---")
    
    # Correct Indentation
    if True:
        print("This line is indented with 4 spaces.")
        print("It belongs to the 'if' block.")
    
    # Potential Error: Mixing tab and spaces (not recommended)
    # Recommended: Always use 4 spaces per indentation level (PEP 8)
    
    try:
        # Example of IndentationError (demonstrated via exec to avoid syntax errors in this file)
        code_with_error = "if True:\nprint('Missing indentation')"
        # exec(code_with_error) # Uncommenting this will raise IndentationError
        print("Indentation defines logic blocks instead of curly braces {} like C++/Java.")
    except Exception as e:
        print(f"Error caught: {e}")

def explain_comments():
    """Shows how to document code correctly."""
    print("\n--- Comments and Docstrings ---")
    
    # This is a single-line comment
    
    """
    This is a multi-line comment (technically a triple-quoted string 
    used as a comment when not assigned to a variable).
    """
    
    print("Comments (started with #) are ignored by the Python interpreter.")
    print("Docstrings (triple quotes) are used for documenting functions and classes.")

def check_case_sensitivity():
    """Python is case-sensitive: 'Variable' and 'variable' are different."""
    print("\n--- Case Sensitivity ---")
    
    message = "Hello"
    Message = "World"
    
    print(f"message: {message}")
    print(f"Message: {Message}")
    
    if message != Message:
        print("Verification: 'message' and 'Message' are distinct variables.")

def main():
    """Driver function for basic concepts."""
    print("🚀 Python Basics Practice")
    print(f"System Version: {sys.version}")
    
    explain_indentation()
    explain_comments()
    check_case_sensitivity()
    
    print("\n--- Summary ---")
    print("1. Indentation is functional, not just for readability.")
    print("2. Python scripts are executed sequentially.")
    print("3. Always follow PEP 8 standards for clean code.")

# Execution Block: Ensures code only runs when script is executed directly
if __name__ == "__main__":
    main()

"""
Input/Output Examples:
Input: None (Direct Execution)
Output:
🚀 Python Basics Practice
System Version: 3.x.x ...
--- Indentation in Python ---
This line is indented with 4 spaces.
It belongs to the 'if' block.
Indentation defines logic blocks instead of curly braces {} like C++/Java.
...
"""
