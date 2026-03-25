"""
📁 04_Loops/control_loop_statements.py
🧠 Topic: Loop Control (break, continue, pass) and the 'else' in Loops

Key Concepts Covered:
1. 'break' - Terminating the entire loop.
2. 'continue' - Skipping the current iteration.
3. 'pass' - A null statement (Place-holder).
4. 'for-else' and 'while-else' - Unique Python features.

Interview Focus:
- What does the 'else' block do in a Python loop? (Only runs if NO 'break' was encountered)
- Difference between 'continue' and 'pass'.
- Using 'break' to optimize searching algorithms (e.g., linear search).
"""

def demonstrate_break_continue():
    """Showing control flows for skipping and termination."""
    print("\n--- Break and Continue Logic ---")
    
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    
    print("Printing only odd numbers (continue if even):")
    for n in numbers:
        if n % 2 == 0:
            continue # Skip the rest of this loop and move to next
        print(n, end=" ")
    print()
    
    print("Terminating loop when number exceeds 5 (break):")
    for n in numbers:
        if n > 5:
            break # Exit the loop completely
        print(n, end=" ")
    print()

def explain_pass_statement():
    """Placeholder for future logic."""
    print("\n--- The 'pass' Statement ---")
    
    for x in range(5):
        if x == 2:
            pass # No operation, used as a placeholder
            print("Passed at 2: Skipping logic but finishing loop block.")
        else:
            print(f"Index: {x}")

def loop_else_feature():
    """Python's unique 'else' block inside loops."""
    print("\n--- Loop-Else Behavior (The 'for-else' block) ---")
    
    # CASE 1: Loop finishes NORMALLY (Else is EXECUTED)
    search_list = [10, 20, 30, 40]
    target = 100
    
    print(f"Searching for {target} in {search_list}...")
    for item in search_list:
        if item == target:
            print("Found!")
            break
    else:
        print(f"RESULT: {target} was NOT found in the list.")
    
    # CASE 2: Loop is BROKEN (Else is SKIPPED)
    target = 20
    print(f"Searching for {target} in {search_list}...")
    for item in search_list:
        if item == target:
            print(f"RESULT: Found {target}. Terminating loop.")
            break
    else:
        print(f"RESULT: {target} not found.")

def infinite_loop_break_example():
    """Common while True pattern with break."""
    print("\n--- While True and Break ---")
    
    counter = 1
    # simulates a loop with a break condition (pseudo-input)
    while True:
        if counter > 3:
            print("Breaking infinite loop at 3.")
            break
        print(f"Iteration: {counter}")
        counter += 1

def main():
    print("🚀 Python Loop Control Practice")
    demonstrate_break_continue()
    explain_pass_statement()
    loop_else_feature()
    infinite_loop_break_example()

if __name__ == "__main__":
    main()

"""
Input/Output Examples:
Output:
Printing only odd numbers (continue if even):
1 3 5 7 9
Terminating loop when number exceeds 5 (break):
1 2 3 4 5
...
RESULT: 100 was NOT found in the list.
...
RESULT: Found 20. Terminating loop.
"""
