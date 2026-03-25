"""
📁 07_Tuples/tuples.py
🧠 Topic: Python Tuples (Immutable Sequences)

Key Concepts Covered:
1. Tuple Creation (Parentheses vs Commas)
2. Immutability (Why use tuples over lists?)
3. Packing & Unpacking (Cool Python feature)
4. Tuple Methods (count, index)
5. NamedTuples (Readable data structures)

Interview Focus:
- Why are tuples FASTER than lists? (Fixed memory size)
- Can you change a list INSIDE a tuple? (Yes, and it's a common trick question)
- How to swap two variables in ONE line? (Unpacking)
"""

from collections import namedtuple

def tuple_creation():
    """Declaring and accessing tuple elements."""
    print("\n--- Tuple Creation and Immutability ---")
    
    # 1. Standard creation
    coords = (10, 20, 30)
    
    # 2. Single element tuple MUST HAVE a trailing comma
    not_a_tuple = ("Hello") # This is just a string in parentheses
    is_a_tuple = ("Hello",) # This is a tuple
    print(f"Type with comma: {type(is_a_tuple).__name__} | Type without comma: {type(not_a_tuple).__name__}")
    
    # 3. Accessing values
    print(f"X-coord: {coords[0]}")
    
    # 4. Immutability
    try:
        # coords[0] = 100
        print(f"Original tuple: {coords}")
        print("Verification: Cannot assign new values (coords[0] = 100 will FAIL).")
    except TypeError as e:
        print(f"Caught ERROR: {e}")

def packing_unpacking():
    """Demonstrating how tuples facilitate variable assignments."""
    print("\n--- Packing and Unpacking ---")
    
    # 1. Packing (Multiple values into one variable)
    p_data = "Alice", 25, "Engineer" # Parentheses are optional during packing
    print(f"Packed Data: {p_data} (Type: {type(p_data).__name__})")
    
    # 2. Unpacking (Extracting values into separate variables)
    name, age, job = p_data
    print(f"Unpacked Variables: name='{name}', age={age}, job='{job}'")
    
    # 3. Variable Swapping (Interview Question)
    x, y = 5, 10
    print(f"Before Swap: x={x}, y={y}")
    x, y = y, x # Values are packed into a tuple and then unpacked back to x and y
    print(f"After Swap:  x={x}, y={y}")

def tricky_mutability():
    """Modifying a mutable object (list) stored within an immutable tuple."""
    print("\n--- Tricky Scenario: List inside a Tuple ---")
    
    nested = (1, 2, [3, 4])
    print(f"Initial: {nested}")
    
    # We cannot replace the list object, but we CAN modify the list ITSELF
    try:
        # nested[2][0] = 100 # Modification within list (Legal)
        # nested[2].append(5) # Adding to list (Legal)
        print("Executing: nested[2].append(5)")
        nested[2].append(5)
        print(f"Modified: {nested}")
    except Exception as e:
        print(f"Caught ERROR: {e}")

def named_tuples_usage():
    """Giving names to indices for better readability."""
    print("\n--- Named Tuples (collections.namedtuple) ---")
    
    # Defining a structure
    Car = namedtuple("Car", "engine color top_speed")
    
    # Creating an instance
    my_test_car = Car(engine="V8", color="Red", top_speed=200)
    
    # Access by index (like normal tuple) OR by attribute name
    print(f"Engine: {my_test_car.engine} | Color: {my_test_car.color}")
    print(f"By Index (0): {my_test_car[0]}")

def main():
    print("🚀 Python Tuples Practice")
    tuple_creation()
    packing_unpacking()
    tricky_mutability()
    named_tuples_usage()

if __name__ == "__main__":
    main()

"""
Input/Output Examples:
Output:
Type with comma: tuple | Type without comma: str
...
Before Swap: x=5, y=10
After Swap:  x=10, y=5
...
Initial: (1, 2, [3, 4])
Modified: (1, 2, [3, 4, 5]) (Proof: Lists remain mutable even inside tuples)
...
"""
