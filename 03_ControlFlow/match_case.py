"""
📁 03_ControlFlow/match_case.py
🧠 Topic: Python Match-Case (Python 3.10+) Structural Pattern Matching

Key Concepts Covered:
1. Basic match-case block
2. OR patterns (|)
3. Wildcards (_) for default case
4. Value Binding and Pattern Matching (Advanced)
5. Conditional Matching (Guards)

Interview Focus:
- How does match-case differ from a switch-case? (Structural Matching)
- Benefits of structural pattern matching over if-elif series.
- Can we match types (class patterns) in match-case? (Yes)
"""

import sys

def basic_day_match(day):
    """Simple day categorization using match."""
    print(f"\n--- Simple Pattern Matching for day: {day} ---")
    
    match day.lower():
        case "monday":
            print("Start of the week!")
        case "friday":
            print("Weekend is near!")
        case "saturday" | "sunday": # OR Pattern
            print("It's the Weekend!")
        case _: # Wildcard (Default Case)
            print("Just another weekday.")

def sequence_pattern_matching(data):
    """Matching the structure of lists/tuples."""
    print(f"\n--- Structure Pattern Matching for data: {data} ---")
    
    match data:
        case [x]: # Match a list with exactly one element
            print(f"List with one element: {x}")
        case [x, y]: # Match a list with exactly two elements
            print(f"List with two elements: {x} and {y}")
        case [first, *rest]: # Match a list with at least one element, capture rest
            print(f"First element is: {first}, Rest of elements: {rest}")
        case _:
            print("No matching structure found.")

def match_with_guards(num):
    """Adding conditions (guards) within a case."""
    print(f"\n--- Matching with Guards for number: {num} ---")
    
    match num:
        case n if n > 100:
            print("Number is exceptionally large.")
        case n if n > 0:
            print("Number is positive.")
        case n if n < 0:
            print("Number is negative.")
        case 0:
            print("Number is exactly Zero.")

def advanced_object_matching(obj):
    """Matching patterns based on values inside objects."""
    print(f"\n --- Point Object Pattern Matching ---")
    
    class Point:
        def __init__(self, x, y):
            self.x = x
            self.y = y
            
    match obj:
        case Point(x=0, y=0):
            print("Origin point at (0,0)")
        case Point(x=x_val, y=0):
            print(f"Point on X-axis at {x_val}")
        case Point(x=0, y=y_val):
            print(f"Point on Y-axis at {y_val}")
        case Point(x=x, y=y):
            print(f"Arbitrary point at ({x}, {y})")

def main():
    # Only works in Python 3.10+
    version = sys.version_info
    if version.major == 3 and version.minor >= 10:
        print("🚀 Python Match-Case (Structural Pattern Matching) Practice")
        basic_day_match("Saturday")
        basic_day_match("Wednesday")
        
        sequence_pattern_matching([1])
        sequence_pattern_matching([10, 20, 30, 40])
        
        match_with_guards(150)
        match_with_guards(-50)
        
        # Object matching
        from collections import namedtuple
        Point = namedtuple("Point", "x y")
        advanced_object_matching(Point(10, 0))
    else:
        print("⚠️ Match-Case requires Python 3.10 or higher.")

if __name__ == "__main__":
    main()

"""
Input/Output Examples:
Output:
--- Simple Pattern Matching for day: Saturday ---
It's the Weekend!
...
--- Structure Pattern Matching for data: [10, 20, 30, 40] ---
First element is: 10, Rest of elements: [20, 30, 40]
...
Point on X-axis at 10
"""
