"""
📁 04_Loops/loops.py
🧠 Topic: Python Loops (for, while, and nested loops)

Key Concepts Covered:
1. 'for' Loop (Iterating over sequences)
2. 'while' Loop (Condition-based iteration)
3. 'range()' Function (Start, Stop, Step)
4. 'enumerate' and 'zip' in Loops
5. Nested Loops (Row-Column logic)

Interview Focus:
- Difference between 'for' and 'while' loops.
- What does range() return in Python 3? (A range object/iterator, not a list)
- How to iterate over multiple lists simultaneously? (zip)
"""

def simple_for_loop():
    """Iterating through strings and lists."""
    print("\n--- Basic 'for' Loop Examples ---")
    
    # 1. String Iteration
    text = "Python"
    print(f"Iterating over string '{text}':")
    for char in text:
        print(char, end=" ")
    print()
    
    # 2. List Iteration
    items = ["Laptop", "Mouse", "Keyboard"]
    print(f"Iterating over list: {items}")
    for item in items:
        print(f"- {item}")

def range_function_deep_dive():
    """Exploring the lazy evaluation of range()."""
    print("\n--- Range Function (start, stop, step) ---")
    
    # range(stop) - 0 to (5-1)
    print(f"range(5): {list(range(5))}")
    
    # range(start, stop) - 2 to (10-1)
    print(f"range(2, 10): {list(range(2, 10))}")
    
    # range(start, stop, step) - Incrementing/Decrementing
    print(f"range(0, 30, 5): {list(range(0, 30, 5))}")
    print(f"range(10, 0, -2): {list(range(10, 0, -2))}")

def advanced_loop_utilities():
    """Using enumerate() and zip() for efficiency."""
    print("\n--- Enumerate and Zip ---")
    
    # 1. Enumerate (Index + Value)
    colors = ["Red", "Green", "Blue"]
    for index, color in enumerate(colors, start=1):
        print(f"Color {index}: {color}")
        
    # 2. Zip (Multiple Lists)
    names = ["Alice", "Bob", "Charlie"]
    scores = [85, 92, 78]
    for name, score in zip(names, scores):
        print(f"{name} scored {score}")

def while_loop_logic():
    """Condition-based loops and handling termination."""
    print("\n--- Basic 'while' Loop ---")
    
    count = 5
    while count > 0:
        print(f"Countdown: {count}")
        count -= 1
    print("Blast Off!")

def nested_loop_matrix():
    """Printing patterns using nested loops."""
    print("\n--- Nested Loops: 3x3 Matrix ---")
    
    for i in range(1, 4): # Rows
        for j in range(1, 4): # Columns
            print(f"({i},{j})", end=" ")
        print() # New line after each row

def main():
    print("🚀 Python Loops (Iteration) Practice")
    simple_for_loop()
    range_function_deep_dive()
    advanced_loop_utilities()
    while_loop_logic()
    nested_loop_matrix()

if __name__ == "__main__":
    main()

"""
Input/Output Examples:
Output:
range(10, 0, -2): [10, 8, 6, 4, 2]
...
Color 1: Red
...
(1,1) (1,2) (1,3) 
(2,1) (2,2) (2,3) 
(3,1) (3,2) (3,3) 
"""
