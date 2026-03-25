"""
📁 15_AdvancedPython/iterators_generators.py
🧠 Topic: Python Advanced (Iterators and Generators)

Key Concepts Covered:
1. Iterator Protocol (__iter__ and __next__)
2. Creating Custom Iterators
3. Generators (yield keyword)
4. Generator Expressions (Memory efficiency)
5. Itertools module (Professional toolset)

Interview Focus:
- Difference between an Iterable and an Iterator? (Structure vs State)
- What is the benefit of yield over return? (Memory saving, lazy evaluation)
- How to create an infinite generator safely? (Inside a while loop)
- What is StopIteration? (Special signal when iterator ends)
"""

import sys

def explain_iterator_protocol():
    """ 
    How Python loops over objects. 
    Any object with __iter__ and __next__ is an iterator.
    """
    print("\n--- The Iterator Protocol ---")
    
    nums = [1, 2, 3]
    
    # 1. Manually converting iterable to iterator
    it = iter(nums)
    print(f"Iterator type: {type(it).__name__}")
    
    # 2. Iterating manually
    print(f"Next value 1: {next(it)}")
    print(f"Next value 2: {next(it)}")
    print(f"Next value 3: {next(it)}")
    
    # 3. Exhausting the iterator
    try:
        print(f"Exhausted value: {next(it)}")
    except StopIteration:
        print("Caught StopIteration: Iterator is empty!")

def explain_generators():
    """ 
    Lazy functions that pause using 'yield'. 
    Generators don't store everything in RAM.
    """
    print("\n--- Generators and 'yield' ---")
    
    def my_generator(limit):
        """ Returns values one-by-one upon request. """
        count = 1
        while count <= limit:
            yield count # pauses here and returns count
            count += 1
            
    gen = my_generator(3)
    
    print(f"Generator type: {type(gen).__name__}")
    for val in gen:
        print(f"Generated: {val}")

def memory_comparison():
    """ Crucial Interview scenario: Large List vs Generator. """
    print("\n--- Memory Performance (Large Data) ---")
    
    # 1. List Comprehension (Entire data in memory)
    limit = 1000000
    L = [x for x in range(limit)]
    print(f"List Size: {sys.getsizeof(L)} bytes")
    
    # 2. Generator Expression (One by one, constant memory)
    G = (x for x in range(limit))
    print(f"Generator Size: {sys.getsizeof(G)} bytes")
    
    print("Optimization: Generators use ~0.01% the memory of a large list!")

def custom_iterator_class():
    """ Creating an iterator from scratch. """
    print("\n--- Custom Iterator Class (Countdown) ---")
    
    class Countdown:
        def __init__(self, start):
            self.current = start
            
        def __iter__(self):
            return self
            
        def __next__(self):
            if self.current <= 0:
                raise StopIteration
            data = self.current
            self.current -= 1
            return data
            
    cd = Countdown(5)
    for num in cd:
        print(num, end=" ")
    print()

def solve_itertools_powers():
    """ Using itertools for professional tasks. """
    print("\n--- Itertools Module ---")
    import itertools
    
    # 1. cycle (infinite loop)
    colors = ["Red", "Green", "Blue"]
    c_cycle = itertools.islice(itertools.cycle(colors), 6) # get first 6
    print(f"Itertools Cycle result: {list(c_cycle)}")
    
    # 2. chain (Join multiple iterables)
    combined = list(itertools.chain([1, 2], ["A", "B"]))
    print(f"Itertools Chain result: {combined}")

def main():
    print("🚀 Python Advanced: Iterators and Generators Practice")
    explain_iterator_protocol()
    explain_generators()
    memory_comparison()
    custom_iterator_class()
    solve_itertools_powers()

if __name__ == "__main__":
    main()

"""
Input/Output Examples:
Output:
Iterator type: list_iterator
Next value 1: 1
Caught StopIteration: Iterator is empty!
...
List Size: 8448728 bytes
Generator Size: 104 bytes
...
Countdown: 5 4 3 2 1
...
"""
