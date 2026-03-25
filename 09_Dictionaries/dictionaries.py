"""
📁 09_Dictionaries/dictionaries.py
🧠 Topic: Python Dictionaries (Key-Value Pair Storage)

Key Concepts Covered:
1. Dictionary Creation and Basic Access
2. Common Dict Methods (get, items, keys, values, pop, update)
3. Dictionary Comprehension (Efficient data mapping)
4. Nested Dictionaries (Complex structure management)
5. Merging Dictionaries (Python 3.9+ features)

Interview Focus:
- Why are dictionary lookups so fast? (Hash Map behavior, O(1) average time)
- Is a dictionary ordered? (Yes, from Python 3.7+ onwards)
- Difference between d['key'] and d.get('key')? (Crucial: Handling missing keys)
- What types of objects can be used as keys? (Only hashable, i.e., immutable)
"""

def dictionary_creation_access():
    """Declaring and accessing dictionary values."""
    print("\n--- Dictionary Basics and Accessing ---")
    
    # 1. Creation styles
    user = {
        "id": 101,
        "name": "Alice",
        "email": "alice@example.com",
        "age": 25
    }
    
    # 2. Key Access (Bracket vs. get())
    print(f"User Name: {user['name']}")
    
    # get() handles missing keys gracefully
    print(f"User City (via .get()): {user.get('city', 'Unknown')}")
    
    try:
        print(f"User City (via []): {user['city']}")
    except KeyError as e:
        print(f"Keyword 'city': Caught ERROR: {e}")

def explore_dictionary_methods():
    """Modifying dictionary contents."""
    print("\n--- Essential Dictionary Methods ---")
    
    stock = {"apples": 10, "bananas": 5, "cherries": 15}
    
    # 1. Accessing keys, values, and items
    print(f"Keys:   {list(stock.keys())}")
    print(f"Values: {list(stock.values())}")
    print(f"Items:  {list(stock.items())}") # Returns list of tuples
    
    # 2. Update with another dictionary
    new_stock = {"bananas": 20, "grapes": 50}
    stock.update(new_stock) # Replaces existing values and adds new keys
    print(f"Updated Stock: {stock}")
    
    # 3. Pop element (removes a key and returns value)
    removed_val = stock.pop("apples")
    print(f"After pop('apples'): {stock} (Removed value: {removed_val})")
    
    # 4. Dictionary Merging (Python 3.9+ ONLY)
    d1 = {"a":1, "b":2}
    d2 = {"b":3, "c":4}
    merged_dict = d1 | d2 # Values from d2 win on key conflicts
    print(f"Merged Dict (d1 | d2): {merged_dict}")

def explain_dict_comprehension():
    """Writing concise loops for mappings."""
    print("\n--- Dictionary Comprehension ---")
    
    # Goal: Map number to its cube
    cubes = {x: x**3 for x in range(1, 6)}
    print(f"Number to Cube mapping: {cubes}")
    
    # Goal: Filter a dictionary
    scores = {"Alice": 85, "Bob": 92, "Charlie": 78, "David": 95}
    high_scorers = {name: score for name, score in scores.items() if score > 90}
    print(f"Students with score > 90: {high_scorers}")

def nested_dictionary_structures():
    """Handling complex records."""
    print("\n--- Nested Dictionaries ---")
    
    company = {
        "HR": {"Lead": "Sarah", "Size": 10},
        "IT": {"Lead": "Mark", "Size": 50, "Tech": ["Python", "AWS", "Docker"]}
    }
    
    print(f"IT Department Lead: {company['IT']['Lead']}")
    print(f"IT tech stack first entry: {company['IT']['Tech'][0]}")

def solve_interview_question():
    """Scenario: Counting frequency of characters in a string."""
    print("\n--- Scenario: Character Frequency Counter ---")
    
    text = "mississippi"
    freq = {}
    
    for char in text:
        # freq[char] = freq.get(char, 0) + 1 # Optimized way
        freq[char] = freq.get(char, 0) + 1
        
    print(f"Frequency of '{text}': {freq}")
    
    # Alternative using collections
    from collections import Counter
    print(f"Frequency using Counter: {dict(Counter(text))}")

def main():
    print("🚀 Python Dictionaries Practice")
    dictionary_creation_access()
    explore_dictionary_methods()
    explain_dict_comprehension()
    nested_dictionary_structures()
    solve_interview_question()

if __name__ == "__main__":
    main()

"""
Input/Output Examples:
Output:
User Name: Alice
User City (via .get()): Unknown
...
Merged Dict (d1 | d2): {'a': 1, 'b': 3, 'c': 4}
...
Frequency of 'mississippi': {'m': 1, 'i': 4, 's': 4, 'p': 2}
"""
