"""
📁 06_Lists/lists.py
🧠 Topic: Python Lists (Dynamic Arrays)

Key Concepts Covered:
1. List Creation and Basic Indexing
2. Common List Methods (append, extend, insert, remove, pop)
3. List Slicing (same pattern as strings)
4. List Comprehension (Pythonic magic)
5. Nested Lists (Multi-dimensional storage)

Interview Focus:
- Difference between append() and extend()? (Very Common)
- Difference between remove() and pop()?
- Benefits of List Comprehension over standard for-loops.
- Are lists mutable? (Yes, and it's their biggest strength)
"""

def list_creation_indexing():
    """Declaring and accessing list elements."""
    print("\n--- List Basics and Indexing ---")
    
    # 1. Creation styles
    my_list = [10, "Python", 20.5, True] # Can contain multiple data types
    print(f"Created list: {my_list}")
    
    # 2. Accessing elements
    print(f"First element: {my_list[0]}")
    print(f"Last element: {my_list[-1]}")
    
    # 3. Mutability: Modifying an existing list
    my_list[1] = "Java"
    print(f"List after modification: {my_list}")

def common_list_methods():
    """Modifying list contents using built-in functions."""
    print("\n--- List Methods (append, extend, insert, etc.) ---")
    
    nums = [1, 2, 3]
    
    # append: Adds ONE element to end
    nums.append(4)
    print(f"After append(4): {nums}")
    
    # extend: Adds multiple elements from another structure (unpacks them)
    nums.extend([5, 6, 7])
    print(f"After extend([5, 6, 7]): {nums}")
    
    # insert: Add element at a specific index
    nums.insert(0, 0) # insert(index, value)
    print(f"After insert(0, 0): {nums}")
    
    # pop: Removes and returns last element (or by index)
    popped_val = nums.pop()
    print(f"After pop(): {nums} (Returned value: {popped_val})")
    
    # remove: Deletes first occurrence of a specific value
    nums.remove(3)
    print(f"After remove(3): {nums}")
    
    # sort: Modifies list in place
    unsorted = [4, 2, 9, 1]
    unsorted.sort()
    print(f"Sorted list: {unsorted}")

def explain_list_comprehension():
    """Writing concise loops for list generation."""
    print("\n--- List Comprehension (Pythonic) ---")
    
    # Goal: Create a list of squares for numbers 0 to 9
    
    # 1. Standard approach
    squares_std = []
    for x in range(10):
        squares_std.append(x**2)
    print(f"Standard approach squares: {squares_std}")
    
    # 2. Comprehension approach
    # [expression for item in iterable if condition]
    squares_comp = [x**2 for x in range(10)]
    print(f"Comp approach squares: {squares_comp}")
    
    # 3. With if-condition
    evens = [x for x in range(21) if x % 2 == 0]
    print(f"Even numbers 0-20: {evens}")

def nested_lists_matrix():
    """Handling matrices and multi-dimensional data."""
    print("\n--- Nested Lists (Matrices) ---")
    
    # 2D Matrix (3x3)
    matrix = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]
    
    print(f"Row 1: {matrix[0]}")
    print(f"Row 2, Column 3: {matrix[1][2]}")
    
    # Nested list comprehension: Flattening a matrix
    flat_list = [num for row in matrix for num in row]
    print(f"Flattened matrix: {flat_list}")

def solve_interview_question():
    """Scenario: How to remove duplicates from a list while keeping order?"""
    print("\n--- Scenario: Remove Duplicates (Maintain Order) ---")
    
    dupes = [1, 5, 2, 1, 9, 5, 2]
    
    # Option 1: Using a temporary list
    seen = []
    for x in dupes:
        if x not in seen:
            seen.append(x)
    print(f"Unique elements: {seen}")
    
    # Option 2: Using dict.fromkeys() (Python 3.7+ keeps insertion order)
    unique_ordered = list(dict.fromkeys(dupes))
    print(f"Unique elements (optimized): {unique_ordered}")

def main():
    print("🚀 Python Lists Practice")
    list_creation_indexing()
    common_list_methods()
    explain_list_comprehension()
    nested_lists_matrix()
    solve_interview_question()

if __name__ == "__main__":
    main()

"""
Input/Output Examples:
Output:
After append(4): [1, 2, 3, 4]
After extend([5, 6, 7]): [1, 2, 3, 4, 5, 6, 7]
...
Standard approach squares: [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
Flattened matrix: [1, 2, 3, 4, 5, 6, 7, 8, 9]
...
"""
