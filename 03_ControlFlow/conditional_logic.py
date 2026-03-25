"""
📁 03_ControlFlow/conditional_logic.py
🧠 Topic: Python Conditional Statements (if, elif, else)

Key Concepts Covered:
1. Basic if-else structures
2. Elif (Shortcut for else-if)
3. Nested Conditions
4. Ternary Operator (One-liner if-else)
5. Short-circuiting and Logical combining

Interview Focus:
- Does Python have a 'switch-case'? (Before 3.10)
- How to write a cleaner alternative using dictionaries.
- Using 'all()' and 'any()' for complex conditions.
"""

def basic_grading_logic(score):
    """Demonstrates if-elif-else hierarchy."""
    print(f"\n--- Basic Grading Logic for score: {score} ---")
    
    # Grading structure
    if score >= 90:
        grade = 'A'
    elif score >= 80:
        grade = 'B'
    elif score >= 70:
        grade = 'C'
    elif score >= 60:
        grade = 'D'
    else:
        grade = 'F'
        
    print(f"Computed Grade: {grade}")

def nested_conditional_checks(num):
    """Nested logic for even/odd and positive/negative."""
    print(f"\n--- Nested Conditionals for number: {num} ---")
    
    if num >= 0:
        if num == 0:
            print("Number is Zero.")
        else:
            print("Number is Positive.")
    else:
        print("Number is Negative.")
        
    # Checking parity (Even/Odd) using modulus
    if num % 2 == 0:
        print(f"{num} is Even.")
    else:
        print(f"{num} is Odd.")

def explain_ternary_operator(age):
    """Single line assignment based on logic."""
    print("\n--- Ternary Operator in Python ---")
    
    # Variable = [Value if True] if [Condition] else [Value if False]
    status = "Adult" if age >= 18 else "Minor"
    
    print(f"Age: {age} | Status: {status}")

def tricky_null_checks():
    """Pythonic way of handling 'none' or 'empty' checks."""
    print("\n--- Pythonic 'Null' Checks (Empty values are falsy) ---")
    
    data_list = []
    message = ""
    value = None
    
    if not data_list:
        print("Verification: Empty list is evaluated as False.")
        
    if not message:
        print("Verification: Empty string is evaluated as False.")
        
    if value is None:
        print("Verification: 'None' type must be checked with 'is'.")

def logic_optimization_hint():
    """Using all() and any() for cleaner multiple logic checks."""
    print("\n--- Using 'all()' and 'any()' for conditions ---")
    
    conditions = [5 > 3, 10 < 20, 100 != 0]
    
    if all(conditions):
        print("Execution: all() - All conditions are TRUE.")
        
    if any([False, True, False]):
        print("Execution: any() - At least one condition is TRUE.")

def main():
    print("🚀 Python Control Flow (Conditionals) Practice")
    basic_grading_logic(85)
    nested_conditional_checks(-7)
    explain_ternary_operator(21)
    tricky_null_checks()
    logic_optimization_hint()

if __name__ == "__main__":
    main()

"""
Input/Output Examples:
Output:
Computed Grade: B
--- Nested Conditionals for number: -7 ---
Number is Negative.
-7 is Odd.
...
Verification: Empty list is evaluated as False.
...
"""
