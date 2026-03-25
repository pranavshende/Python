"""
📁 10_Functions/basic_functions.py
🧠 Topic: Python Functions (Reusable Code Blocks)

Key Concepts Covered:
1. Function Definition (def, return)
2. Global vs Local Scope
3. Positional and Keyword Arguments
4. Default Parameters
5. Docstrings for Documentation

Interview Focus:
- Difference between parameters and arguments?
- What happens if a function has NO return? (Returns 'None' implicitly)
- Why use default arguments? (Flexible calls)
- Tricky: Should you use a list as a default argument? (CRITICAL: No, use None)
"""

# Global variable
total_calls = 0

def greet_user(name, greeting="Hello"): # default parameter: greeting
    """ Greets a user with a specific message. """
    global total_calls # Using the global variable
    total_calls += 1
    
    return f"{greeting}, {name}!"

def calculate_area(length, width):
    """ Positional vs Keyword Arguments. """
    return length * width

def modify_outside_variable(val):
    """ Demonstrates scope. """
    # val is local to this function
    val = val * 2
    print(f"Inside function (modified val): {val}")

def explain_variable_scope():
    """ Showing the distinction between Local and Global. """
    print("\n--- Variable Scope (Global vs Local) ---")
    
    # Global: total_calls
    # Local: current_user (only inside this function)
    current_user = "Pranav" 
    
    print(f"Global total_calls: {total_calls}")
    print(f"Local current_user: {current_user}")

def solve_default_args_trap():
    """ 
    CRITICAL INTERVIEW TOPIC: 
    Mutable default arguments are shared across calls.
    Always use None instead of [].
    """
    print("\n--- The Mutable Default Argument Trap ---")
    
    # WRONG way (don't do this)
    def append_to_list_broken(element, my_list=[]):
        my_list.append(element)
        return my_list
        
    print(f"Call 1: {append_to_list_broken('apple')}")
    print(f"Call 2: {append_to_list_broken('banana')}") # Unexpectedly adds to previous list
    
    # RIGHT way
    def append_to_list_fixed(element, my_list=None):
        if my_list is None:
            my_list = []
        my_list.append(element)
        return my_list
        
    print(f"Call 1 (fixed): {append_to_list_fixed('apple')}")
    print(f"Call 2 (fixed): {append_to_list_fixed('banana')}") # New list created correctly

def main():
    print("🚀 Python Basic Functions Practice")
    
    # 1. Basic Function Call
    msg = greet_user("Alice")
    print(f"Basic call with default greeting: {msg}")
    
    # 2. Overriding default greeting
    msg_custom = greet_user("Bob", "Good Morning")
    print(f"Custom greeting call: {msg_custom}")
    
    # 3. Positional vs Keyword
    print(f"Positional call (10, 5): {calculate_area(10, 5)}")
    print(f"Keyword call (width=5, length=10): {calculate_area(width=5, length=10)}")
    
    # 4. Scope
    x = 100
    modify_outside_variable(x)
    print(f"Outside function (x remains): {x}")
    
    explain_variable_scope()
    solve_default_args_trap()

if __name__ == "__main__":
    main()

"""
Input/Output Examples:
Output:
Basic call with default greeting: Hello, Alice!
Custom greeting call: Good Morning, Bob!
...
Call 1: ['apple']
Call 2: ['apple', 'banana'] (Bug: Shared reference in defaults)
Call 1 (fixed): ['apple']
Call 2 (fixed): ['banana'] (Correct: Independent reference)
"""
