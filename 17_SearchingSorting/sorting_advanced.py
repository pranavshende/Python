"""
📁 17_SearchingSorting/sorting_advanced.py
🧠 Topic: Advanced Sorting (Insertion Sort and Merge Sort)

Key Concepts Covered:
1. Insertion Sort (Sorting like a card hand)
2. Merge Sort (Divide and Conquer - Stable sort)
3. Time Complexity: O(N^2) vs O(N log N)
4. Stability in Sorting (Maintaining order of equal elements)

Interview Focus:
- Why use Insertion Sort for small arrays? (Lower constant overhead)
- Why is Merge Sort preferred for Linked Lists? (Sequential access)
- Difference between In-place and Out-of-place sorting?
- Understanding the merge() logic process.
"""

def insertion_sort(items):
    """ 
    O(N^2) Complexity: Building a sorted sub-list one element at a time. 
    Great for nearly sorted data!
    """
    print("\n--- Running Insertion Sort ---")
    length = len(items)
    
    for i in range(1, length):
        current_val = items[i]
        j = i - 1
        
        # Move elements of items[0..i-1] that are > current_val to one position ahead
        while j >= 0 and items[j] > current_val:
            items[j + 1] = items[j]
            j = j - 1
        items[j + 1] = current_val
        
    return items

def merge_sort(items):
    """ 
    O(N log N) Complexity: Recursive 'Divide and Conquer'. 
    Stable and consistent!
    """
    if len(items) <= 1:
        return items
        
    # 1. DIVIDE: Find mid point
    mid_idx = len(items) // 2
    left_side = items[:mid_idx]
    right_side = items[mid_idx:]
    
    # 2. CONQUER: Recursively sort halves
    left_sorted = merge_sort(left_side)
    right_sorted = merge_sort(right_side)
    
    # 3. COMBINE: Merge the sorted halves
    return merge(left_sorted, right_sorted)

def merge(left_list, right_list):
    """ Helper to merge two sorted lists. """
    merged_results = []
    idx_left = 0
    idx_right = 0
    
    # Compare elements from both lists
    while idx_left < len(left_list) and idx_right < len(right_list):
        if left_list[idx_left] < right_list[idx_right]:
            merged_results.append(left_list[idx_left])
            idx_left = idx_left + 1
        else:
            merged_results.append(right_list[idx_right])
            idx_right = idx_right + 1
            
    # Add remaining elements
    merged_results.extend(left_list[idx_left:])
    merged_results.extend(right_list[idx_right:])
    return merged_results

def main():
    print("🚀 Python Advanced Sorting Practice")
    test_data = [38, 27, 43, 3, 9, 82, 10]
    
    # 1. Insertion Sort
    print(f"Insertion Sort result: {insertion_sort(test_data.copy())}")
    
    # 2. Merge Sort
    print("\n--- Running Merge Sort (Recursive) ---")
    print(f"Merge Sort result:     {merge_sort(test_data.copy())}")

if __name__ == "__main__":
    main()

"""
Input/Output Examples:
Output:
Insertion Sort result: [3, 9, 10, 27, 38, 43, 82]
Merge Sort result:     [3, 9, 10, 27, 38, 43, 82]
"""
