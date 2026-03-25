"""
📁 15_AdvancedPython/decorators_closures.py
🧠 Topic: Python Advanced (Decorators and Closures)

Key Concepts Covered:
1. Higher-Order Functions (Functions as objects)
2. Closures (Functions remembering their outer scope)
3. Decorators (Modifying behavior with @ syntax)
4. Wrappers and inner functions
5. functools.wraps (Best practice: keeping docstrings)
6. Decorators with arguments

Interview Focus:
- What is a decorator? (Design pattern: Wrapper to add functionality)
- What is a closure? (Inner function + outer variable state)
- Practical use cases for decorators? (Logging, Timing, Execution control, Auth checks)
- Why use @functools.wraps? (Preserving metadata of the original function)
"""

import time
import functools

# 1. CLOSURES (A function that 'remembers' its creation context)
def power_factory(exponent):
    """ Returns a function configured for a specific power. """
    def compute(base):
        # remembers 'exponent' from outer scope
        return base ** exponent
    return compute

# 2. DECORATORS (A function that WRAPS another function)
def logger_decorator(func):
    """ Simple decorator to log function calls. """
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print(f"[LOG] Executing: {func.__name__}...")
        result = func(*args, **kwargs)
        print(f"[LOG] Finished execution of {func.__name__}.")
        return result
    return wrapper

@logger_decorator
def greet(name):
    """ A simple greeting function. """
    print(f"Hello, {name}!")

# 3. ADVANCED DECORATOR: Timing (Practical example)
def timer_decorator(func):
    """ Performance tracking decorator. """
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        result = func(*args, **kwargs)
        end = time.perf_counter()
        print(f"Function {func.__name__} took {(end - start):.4f} seconds.")
        return result
    return wrapper

@timer_decorator
def expensive_task(n):
    """ Simulates some time-consuming logic. """
    time.sleep(n)
    return f"Finished task with load {n}"

# 4. DECORATORS WITH ARGUMENTS (Double-layered wrapper)
def repeat_decorator(times):
    """ Returns a decorator that runs the function N times. """
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            for _ in range(times):
                res = func(*args, **kwargs)
            return res
        return wrapper
    return decorator

@repeat_decorator(times=3)
def say_hi():
    print("Welcome!")

def explain_closures():
    """ Showing the 'memory' of closures. """
    print("\n--- Closures (The 'Memory' of functions) ---")
    
    square = power_factory(2)
    cube = power_factory(3)
    
    print(f"5 Square: {square(5)}")
    print(f"2 Cube:   {cube(2)}")

def explain_decorators():
    """ Showing how @ syntax works. """
    print("\n--- Basic and Advanced Decorators ---")
    
    # 1. Logger decorator
    greet("Pranav")
    
    # 2. Timer decorator
    expensive_task(1)
    
    # 3. Meta-argument decorator
    print("Running @repeat_decorator(3)...")
    say_hi()

def demonstrate_metadata_issue():
    """ Why we use @functools.wraps. """
    print("\n--- Metadata Preservation (wraps) ---")
    
    # Check the docstring of our decorated 'greet'
    print(f"Function Name: {greet.__name__}")
    print(f"Function Doc:  {greet.__doc__}")

def main():
    print("🚀 Python Advanced: Decorators and Closures Practice")
    explain_closures()
    explain_decorators()
    demonstrate_metadata_issue()

if __name__ == "__main__":
    main()

"""
Input/Output Examples:
Output:
5 Square: 25
2 Cube:   8
...
[LOG] Executing: greet...
Hello, Pranav!
[LOG] Finished execution of greet.
...
Function expensive_task took 1.0003 seconds.
...
Function Name: greet
Function Doc:  A simple greeting function. (Saved by wraps!)
"""
