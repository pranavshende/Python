"""
📁 01_Basics/io_casting.py
🧠 Topic: Input/Output and Type Casting

Key Concepts Covered:
1. Standard Input (input())
2. Standard Output (print() with modifiers)
3. Type Conversion (Implicit vs. Explicit Casting)
4. Handling Input Errors (Basic try-except)

Interview Focus:
- Does input() always return a string?
- Difference between print(f"...") and print("...".format())
- Implicit type conversion in expressions.
- Handling ValueError during casting.
"""

def explain_input_output():
    """Demonstrates input capture and formatted output."""
    print("\n--- Standard Input and Output ---")
    
    # Python 3 inputs return STRINGS by default
    user_name = "User" # hardcoding for demonstration, input() can't be used async
    user_age = 25
    
    # print() modifiers: sep, end
    print("Welcome", user_name, sep=" - ", end="!\n")
    
    # F-Strings (most efficient and readable, Python 3.6+)
    print(f"User: {user_name} | Age: {user_age}")
    
    # Separators: Joining elements with a comma
    print("Apple", "Banana", "Cherry", sep=", ")

def demonstrate_casting():
    """Shows explicit and implicit type casting."""
    print("\n--- Type Casting and Conversion ---")
    
    # 1. Implicit Conversion (Automatic)
    num_int = 10
    num_float = 20.5
    result = num_int + num_float 
    print(f"Implicit addition ({num_int} + {num_float}): {result} (Type: {type(result).__name__})")
    
    # 2. Explicit Casting (Manual)
    s_val = "100"
    casted_int = int(s_val)
    casted_float = float(s_val)
    
    print(f"String to Int: {casted_int} | String to Float: {casted_float}")
    
    # Casting integers to complex
    c_val = complex(casted_int)
    print(f"Int to Complex: {c_val}")
    
    # Boolean casting (The 'Truthy' and 'Falsy' concept)
    print(f"bool(0): {bool(0)} | bool(1): {bool(1)}")
    print(f"bool(''): {bool('')} | bool('text'): {bool('text')}")

def error_handling_casting():
    """Shows safe casting to prevent runtime crashes."""
    print("\n--- Safe Type Casting (Exception Handling) ---")
    
    invalid_input = "ABC123"
    
    try:
        print(f"Attempting to cast '{invalid_input}' to integer...")
        converted = int(invalid_input)
        print(f"Successfully converted: {converted}")
    except ValueError as e:
        print(f"Caught ERROR: Cannot convert non-numeric string to integer. ({e})")
    finally:
        print("Casting attempt completed.")

def solve_interview_question():
    """Scenario: How to input multiple values in a single line?"""
    print("\n--- Scenario: Multiple Inputs on One Line ---")
    
    # Mocking single line input: "10 20 30"
    mock_input = "10 20 30"
    x, y, z = map(int, mock_input.split())
    
    print(f"Parsed variables: x={x}, y={y}, z={z}")
    print(f"Sum of variables: {x + y + z}")

def main():
    print("🚀 Python Input/Output and Casting Practice")
    explain_input_output()
    demonstrate_casting()
    error_handling_casting()
    solve_interview_question()

if __name__ == "__main__":
    main()

"""
Input/Output Examples:
Output:
Welcome - User!
User: User | Age: 25
...
Implicit addition (10 + 20.5): 30.5 (Type: float)
String to Int: 100 | String to Float: 100.0
...
bool(0): False | bool(1): True
bool(''): False | bool('text'): True
...
Caught ERROR: Cannot convert non-numeric string to integer. ...
Parsed variables: x=10, y=20, z=30
Sum of variables: 60
"""
