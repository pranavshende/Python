"""
📁 13_ExceptionHandling/exceptions.py
🧠 Topic: Python Exception Handling (try, except, finally)

Key Concepts Covered:
1. Basic try-except block
2. Multiple except clauses (Specific vs Universal)
3. Catching All Exceptions (Exception as e)
4. The 'else' and 'finally' blocks
5. Raising exceptions (raise)
6. Custom Exception classes (Inheritance from Exception)

Interview Focus:
- Why use finally? (Cleaning up resources: closing files, database connections)
- Difference between 'except' and 'except Exception'? (Selective catching)
- What is a Custom Exception and why use it? (Domain-specific error handling)
- Purpose of the 'else' block in try-finally? (Runs only if no error occurred)
"""

def basic_exception_handling():
    """Handling common ZeroDivisionError & ValueError."""
    print("\n--- Basic Try-Except ---")
    
    data = [10, 5, 0, "A", 2]
    
    for val in data:
        try:
            print(f"Calculating 100 / {val}...")
            result = 100 / int(val)
            print(f"Success! Result: {result}")
            
        except ZeroDivisionError:
            print(f"Caught ERROR: Cannot divide by ZERO for input: {val}")
            
        except ValueError:
            print(f"Caught ERROR: Input '{val}' is not a valid number.")
            
        except Exception as e:
            print(f"Caught UNKNOWN ERROR: {e}")

def explain_else_finally():
    """Showing execution flow for success and always-run blocks."""
    print("\n--- Try-Except-Else-Finally ---")
    
    def divide_logic(a, b):
        try:
            res = a / b
        except ZeroDivisionError:
            print(f"Division by Zero! (Inputs: {a}, {b})")
        else:
            # runs ONLY if code in 'try' succeeds
            print(f"SUCCESS: Result is {res}")
        finally:
            # ALWAYS runs (no matter what happened)
            print("Cleanup: closing division module...")
            
    # Case 1: Success
    divide_logic(10, 2)
    
    # Case 2: Failure
    divide_logic(10, 0)

def demonstrate_raising_exception():
    """Forcing an error based on business logic."""
    print("\n--- Raising Exceptions (raise) ---")
    
    def check_age(age):
        if age < 0:
            raise ValueError("Age cannot be negative!")
        if age < 18:
            print("Access Denied: Minor.")
        else:
            print("Access Granted: Adult.")
            
    try:
        check_age(-5)
    except ValueError as e:
        print(f"Caught Logic ERROR: {e}")

class InsufficientFundsError(Exception):
    """Creating our OWN exception for specific use cases."""
    pass

def handle_custom_exception(balance, withdrawal):
    """Handling domain-specific errors (Banking Example)."""
    print("\n--- Custom Exception Handling ---")
    
    try:
        if withdrawal > balance:
            raise InsufficientFundsError(f"Attempt to withdraw ${withdrawal} failed. Current balance: ${balance}")
        print(f"Success! Remaining balance: ${balance - withdrawal}")
    except InsufficientFundsError as e:
        print(f"BANKING ERROR: {e}")

def main():
    print("🚀 Python Exception Handling Practice")
    basic_exception_handling()
    explain_else_finally()
    demonstrate_raising_exception()
    handle_custom_exception(500, 1000)

if __name__ == "__main__":
    main()

"""
Input/Output Examples:
Output:
Caught ERROR: Cannot divide by ZERO for input: 0
Caught ERROR: Input 'A' is not a valid number.
...
SUCCESS: Result is 5.0
Cleanup: closing division module...
...
BANKING ERROR: Attempt to withdraw $1000 failed. ...
"""
