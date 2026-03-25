"""
📁 17_SearchingSorting/sorting.py
🧠 Topic: Python Sorting Algorithms (Bubble, Selection, Insertion, Merge, Quick Sort)

Key Concepts Covered:
1. Bubble Sort (Compare adjacent elements)
2. Selection Sort (Keep track of minimum)
3. Insertion Sort (Build sorted array one-by-one)
4. Merge Sort (Divide and Conquer - Recursive)
5. Quick Sort (Pivoting - Recursive)
6. Python's Timsort (.sort() / sorted()) - Optimized real-world algorithm

Interview Focus:
- Which sort is most efficient for large data? (Merge/Quick Sort)
- Space complexity of Merge Sort? (O(N) - auxiliary space)
- Difference between Bubble and Quick Sort? (O(N^2) vs O(N log N))
- Why is Timsort so popular? (Adaptive, Stable, and efficient)
"""

def bubble_sort(data):
    """ O(N^2) Complexity: Sinking the largest element to the end. """
    print("\n--- Running Bubble Sort ---")
    n = len(data)
    
    # 1. Loop through all elements
    for i in range(n):
        # 2. Optimized: Skip sorted elements from end
        for j in range(0, n - i - 1):
            # 3. Swap if current is larger than next
            if data[j] > data[j+1]:
                data[j], data[j+1] = data[j+1], data[j]
    return data

def selection_sort(data):
    """ O(N^2) Complexity: Repeatedly finding the MINIMUM element. """
    print("\n--- Running Selection Sort ---")
    n = len(data)
    
    for i in range(n):
        min_idx = i
        # 1. Find min in remaining list
        for j in range(i+1, n):
            if data[j] < data[min_idx]:
                min_idx = j
                
        # 2. Swap min with first element of unsorted part
        data[i], data[min_idx] = data[min_idx], data[i]
    return data

def quick_sort(data):
    """ O(N log N) Average Complexity: Using a Pivot to partition. """
    # 1. Base case: Single element already sorted
    if len(data) <= 1:
        return data
        
    # 2. Choose pivot (usually middle or end)
    pivot = data[len(data) // 2]
    
    # 3. Partition: Left < Pivot, Middle == Pivot, Right > Pivot
    left = [x for x in data if x < pivot]
    middle = [x for x in data if x == pivot]
    right = [x for x in data if x > pivot]
    
    # 4. Recursively sort left and right
    return quick_sort(left) + middle + quick_sort(right)

def interview_scenario_built_in():
    """ 
    Practical Tip: Use Python's built-in sorted() for production. 
    It uses Timsort (Hybrid of Insertion and Merge).
    """
    print("\n--- Python's Built-in Timsort ---")
    
    data = [4, 2, 9, 1, 5, 6]
    
    # .sort() modifies in place
    # sorted() creates a new list
    new_data = sorted(data, reverse=True)
    print(f"Data sorted in reverse: {new_data}")

def main():
    print("🚀 Python Sorting Algorithms Practice")
    
    test_data = [64, 34, 25, 12, 22, 11, 90]
    
    # 1. Bubble Sort
    print(bubble_sort(test_data.copy()))
    
    # 2. Selection Sort
    print(selection_sort(test_data.copy()))
    
    # 3. Quick Sort (Recursive)
    print("\n--- Running Quick Sort (Recursive) ---")
    print(quick_sort(test_data.copy()))
    
    # 4. Built-in
    interview_scenario_built_in()

if __name__ == "__main__":
    main()

"""
Input/Output Examples:
Output:
Running Bubble Sort
[11, 12, 22, 25, 34, 64, 90]
...
Running Selection Sort
[11, 12, 22, 25, 34, 64, 90]
...
Running Quick Sort (Recursive)
[11, 12, 22, 25, 34, 64, 90]
...
"""
