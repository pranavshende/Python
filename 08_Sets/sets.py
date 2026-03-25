"""
📁 08_Sets/sets.py
🧠 Topic: Python Sets (Unordered Collections of Unique Elements)

Key Concepts Covered:
1. Set Creation and Basic Properties
2. Common Set Methods (add, remove, discard, clear)
3. Mathematical Set Operations (Union, Intersection, etc.)
4. Comparison of Set vs List vs Tuple
5. Frozen Sets (Immutable Sets)

Interview Focus:
- Why use sets instead of lists? (Duplicate removal, O(1) membership check)
- Difference between discard() and remove()? (Handling errors)
- How to perform union and intersection? (Using | and & operators)
- Can sets contain mutable objects? (No, set elements must be hashable)
"""

def set_creation_properties():
    """Declaring and accessing set elements."""
    print("\n--- Set Creation and Properties ---")
    
    # 1. Creation styles
    s1 = {1, 2, 3, 4, 1, 2} # Duplicates are automatically removed
    s2 = set([10, 20, 30, 40, 50, 10]) # Creating from a list
    
    # 2. Key properties
    print(f"Set s1: {s1} (Only unique values kept)")
    print(f"Set s2: {s2}")
    
    # 3. Membership checking (extremely FAST - O(1))
    print(f"Is 3 in s1? {3 in s1}")
    
    # 4. NOTE: Sets are UNORDERED (Cannot access by index s1[0] will FAIL)
    try:
        # s1[0] = 100
        print("Verification: Cannot index or slice sets.")
    except TypeError as e:
        print(f"Caught ERROR: {e}")

def modify_set_contents():
    """Add, Update, Remove, Discard operations."""
    print("\n--- Modifying Sets ---")
    
    chars = {"A", "B", "C"}
    
    # 1. Add single element
    chars.add("D")
    
    # 2. Update with multiple elements (from list/tuple)
    chars.update(["E", "F"])
    print(f"Set after Add/Update: {chars}")
    
    # 3. Discard vs Remove (Interview Question)
    chars.discard("Z") # Does NOTHING if Z is missing (Safe)
    print("discard('Z'): Safe - No error.")
    
    try:
        chars.remove("Z") # Raises KeyError if missing
    except KeyError:
        print("remove('Z'): FAILED - Raises KeyError if not found.")
        
    # 4. Pop (removes a RANDOM element since sets are unordered)
    val = chars.pop()
    print(f"popped value (random): {val} | Remaining: {chars}")

def mathematical_operations():
    """Power of sets: Venn-diagram like logic."""
    print("\n--- Mathematical Set Operations ---")
    
    A = {1, 2, 3, 4, 5}
    B = {4, 5, 6, 7, 8}
    
    # 1. Union (Elements in A OR B)
    print(f"A | B (Union): {A | B}")
    
    # 2. Intersection (Elements in A AND B)
    print(f"A & B (Intersection): {A & B}")
    
    # 3. Difference (Elements in A but NOT in B)
    print(f"A - B (Difference): {A - B}")
    
    # 4. Symmetric Difference (Elements in EITHER A or B, but NOT BOTH)
    print(f"A ^ B (Symmetric Diff): {A ^ B}")

def frozen_sets_usage():
    """Immutable version of sets."""
    print("\n--- Frozen Sets (Immutable Sets) ---")
    
    immutable_set = frozenset([1, 2, 3, 4])
    print(f"Frozen Set: {immutable_set}")
    
    try:
        # immutable_set.add(5)
        print("Verification: Cannot add/modify a frozenset.")
    except AttributeError as e:
        print(f"Caught ERROR: {e}")

def solve_interview_question():
    """Scenario: How to check if all elements of A are inside B?"""
    print("\n--- Scenario: Subsets and Supersets ---")
    
    A = {1, 2, 3}
    B = {1, 2, 3, 4, 5}
    
    print(f"Is A a subset of B? {A.issubset(B)}")
    print(f"Is B a superset of A? {B.issuperset(A)}")

def main():
    print("🚀 Python Sets Practice")
    set_creation_properties()
    modify_set_contents()
    mathematical_operations()
    frozen_sets_usage()
    solve_interview_question()

if __name__ == "__main__":
    main()

"""
Input/Output Examples:
Output:
Set s1: {1, 2, 3, 4} (Only unique values kept)
...
A | B (Union): {1, 2, 3, 4, 5, 6, 7, 8}
A & B (Intersection): {4, 5}
A - B (Difference): {1, 2, 3}
...
"""
