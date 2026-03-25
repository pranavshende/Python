"""
📁 10_Functions/args_kwargs.py
🧠 Topic: Python Advanced Function Arguments (*args and **kwargs)

Key Concepts Covered:
1. *args (Variable-length positional arguments)
2. **kwargs (Variable-length keyword arguments)
3. Argument Packing and Unpacking
4. Mandatory Keyword-only Arguments

Interview Focus:
- What's the benefit of *args and **kwargs? (Flexibility for wrappers/mixins)
- Which one comes first if both are used? (args before kwargs)
- Can we unpack a list as arguments into a function? (Yes, using *)
- Difference between *args and a simple list? (Packing behavior)
"""

def demonstrate_args(*args):
    """How to pass multiple values into a function."""
    print("\n--- *args (Positional Argument Packing) ---")
    
    # args is a TUPLE containing all arguments passed
    print(f"args type: {type(args).__name__}")
    print(f"Values passed: {args}")
    
    total = sum(args) # Since it's a tuple, we can sum it
    print(f"Sum of arguments: {total}")

def demonstrate_kwargs(**kwargs):
    """How to pass multiple key-value pairs into a function."""
    print("\n--- **kwargs (Keyword Argument Packing) ---")
    
    # kwargs is a DICTIONARY containing all key-value arguments
    print(f"kwargs type: {type(kwargs).__name__}")
    
    for key, val in kwargs.items():
        print(f"Key: {key:8} | Value: {val}")

def combined_arguments(name, *args, **kwargs):
    """Combining all types in the correct order."""
    print("\n--- Combining Argument Types (name, *args, **kwargs) ---")
    
    print(f"Standard Mandatory Arg: {name}")
    print(f"Optional Args (*args): {args}")
    print(f"Optional Keywords (**kwargs): {kwargs}")

def argument_unpacking():
    """Showing how to UNPACK structures into call signals."""
    print("\n--- Argument Unpacking (* and **) ---")
    
    def calculate_tax(base, rate, discount):
        return (base * rate) - discount
        
    nums = [1000, 0.1, 20]
    # unpacking list into positional args
    result = calculate_tax(*nums) # equivalent to calculate_tax(1000, 0.1, 20)
    print(f"Unpacked list result: {result}")
    
    params = {"base": 2000, "rate": 0.05, "discount": 50}
    # unpacking dictionary into keyword args
    result = calculate_tax(**params) # equivalent to calculate_tax(base=2000, ...)
    print(f"Unpacked dict result: {result}")

def keyword_only_args(a, b, *, debug=False):
    """Forcing certain parameters to be keywords."""
    print(f"\n--- Keyword-only Parameters (debug={debug}) ---")
    
    # The '*' in parameters forces all AFTER it to be keyword-only
    print(f"Sum of {a} and {b}: {a + b}")

def main():
    print("🚀 Python *args and **kwargs Practice")
    
    # 1. *args
    demonstrate_args(10, 20, 30, 40)
    
    # 2. **kwargs
    demonstrate_kwargs(id=1, name="Admin", role="Superuser")
    
    # 3. Combined
    combined_arguments("System-Root", 1, 2, 3, status="Active", log_level=10)
    
    # 4. Unpacking
    argument_unpacking()
    
    # 5. Mandatory keywords
    keyword_only_args(10, 20, debug=True)
    # keyword_only_args(10, 20, True) # Will FAIL (TypeError: takes 2 positional arguments ...)

if __name__ == "__main__":
    main()

"""
Input/Output Examples:
Output:
args type: tuple
Values passed: (10, 20, 30, 40)
...
Key: id       | Value: 1
Key: name     | Value: Admin
...
Unpacked list result: 80.0
...
"""
