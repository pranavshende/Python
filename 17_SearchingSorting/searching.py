"""
📁 17_SearchingSorting/searching.py
🧠 Topic: Python Searching Algorithms (Linear and Binary Search)

Key Concepts Covered:
1. Linear Search (Check every element)
2. Binary Search (Requires sorted data)
3. Time Complexity Analysis (O(N) vs O(log N))
4. Space Complexity Analysis
5. Recursive vs Iterative Binary Search

Interview Focus:
- When to use Linear Search? (Unsorted or very small collection)
- Pre-requisite of Binary Search? (Must be sorted)
- Why is Binary Search faster? (Eliminates half of the work every step)
- Best case / Worst case time complexity?
"""

def linear_search(data, target):
    """ O(N) Complexity: Searching by checking every element. """
    print(f"\n--- Linear Search for {target} ---")
    
    for index, val in enumerate(data):
        if val == target:
            return f"FOUND at index: {index}"
            
    return "RESULT: Not Found."

def binary_search_iterative(data, target):
    """ O(log N) Complexity: Using 'Divide and Conquer'. """
    print(f"\n--- Binary Search (Iterative) for {target} ---")
    
    # 1. Start pointers at ends
    low = 0
    high = len(data) - 1
    
    while low <= high:
        # 2. Find the mid point (using integer division)
        mid = (low + high) // 2
        
        # 3. Check mid
        if data[mid] == target:
            return f"FOUND at index: {mid}"
            
        # 4. If target is GREATER, ignore left half
        elif data[mid] < target:
            low = mid + 1
            
        # 5. If target is LESS, ignore right half
        else:
            high = mid - 1
            
    return "RESULT: Not Found."

def binary_search_recursive(data, target, low, high):
    """ Recursive approach to Binary Search. """
    
    # 1. Base case: Not found
    if low > high:
        return "RESULT: Not Found."
        
    # 2. Calculate mid
    mid = (low + high) // 2
    
    # 3. Correct match
    if data[mid] == target:
        return f"FOUND at index: {mid}"
    
    # 4. Recursive calls
    elif data[mid] < target:
        return binary_search_recursive(data, target, mid + 1, high) # search right
    else:
        return binary_search_recursive(data, target, low, mid - 1) # search left

def main():
    print("🚀 Python Searching Algorithms Practice")
    
    unsorted_data = [20, 10, 5, 50, 40]
    sorted_data = [1, 5, 10, 15, 20, 25, 30]
    
    # 1. Linear Search
    print(linear_search(unsorted_data, 50))
    print(linear_search(unsorted_data, 99)) # Missing
    
    # 2. Binary Search (Iterative)
    # Binary search WILL fail on unsorted data without prior sorting!
    print(binary_search_iterative(sorted_data, 15))
    
    # 3. Binary Search (Recursive)
    print("\n--- Binary Search (Recursive) for 25 ---")
    print(binary_search_recursive(sorted_data, 25, 0, len(sorted_data)-1))

if __name__ == "__main__":
    main()

"""
Input/Output Examples:
Output:
Linear Search for 50
FOUND at index: 3
...
Binary Search (Iterative) for 15
FOUND at index: 3
...
Binary Search (Recursive) for 25
FOUND at index: 5
"""
