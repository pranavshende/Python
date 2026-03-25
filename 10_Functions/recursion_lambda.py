"""
📁 10_Functions/recursion_lambda.py
🧠 Topic: Python Advanced Functions (Recursion, Lambda, and Higher-Order)

Key Concepts Covered:
1. Recursion (Function calling itself)
2. Base Case vs Recursive Case
3. Lambda Functions (Anonymous one-liners)
4. Higher-Order Functions (map, filter, sorted)
5. Memoization (Performance optimization)

Interview Focus:
- Why is a base case critical? (Prevent recursion depth error)
- Benefit of recursion? (Clean, mathematical solutions like Factorial, Fibonacci)
- When NOT to use recursion? (High overhead, memory limits)
- What is a Lambda function?
"""

import sys

def explain_recursion_factorial(n):
    """Solving Factorial problem using the power of recursion."""
    # BASE CASE
    if n == 0 or n == 1:
        return 1
        
    # RECURSIVE CASE
    # n! = n * (n-1)!
    return n * explain_recursion_factorial(n-1)

def fibonacci_with_recursion(n):
    """Classical Fibonacci using recursion (Wait - this is inefficient!)."""
    # 0, 1, 1, 2, 3, 5, 8, 13...
    if n <= 1:
        return n
    return fibonacci_with_recursion(n-1) + fibonacci_with_recursion(n-2)

def recursive_sum(numbers):
    """Summing values in a list recursively."""
    if not numbers:
        return 0
    return numbers[0] + recursive_sum(numbers[1:])

def explain_lambda_functions():
    """Declaring anonymous functions in line."""
    print("\n--- Lambda (Anonymous Functions) ---")
    
    # 1. Simple addition
    add_lambda = lambda x, y: x + y
    print(f"Adding 5 and 10 via lambda: {add_lambda(5, 10)}")
    
    # 2. Square calculation
    square_lambda = lambda x: x**2
    print(f"Square of 8 via lambda: {square_lambda(8)}")

def higher_order_functions():
    """Using functions that take other functions as arguments."""
    print("\n--- Higher-Order Functions: map, filter, sorted ---")
    
    nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    
    # 1. map() - Transforming each element
    # Goal: Double every number
    doubled = list(map(lambda x: x * 2, nums))
    print(f"map result  (Doubled): {doubled}")
    
    # 2. filter() - Keeping only certain elements
    # Goal: Keep only even numbers
    evens = list(filter(lambda x: x % 2 == 0, nums))
    print(f"filter result (Evens): {evens}")
    
    # 3. sorted() with key - Custom sorting logic
    words = ["apple", "Kiwi", "banana", "Cherry"]
    # Case-insensitive sorting
    print(f"Sorted words (Custom Key): {sorted(words, key=lambda x: x.lower())}")

def solve_interview_scenarios():
    """ 
    Practical scenarios: Recursion Depth and Tail Recursion. 
    Python has a limited recursion depth (default ~1000).
    """
    print("\n--- Recursion Scenarios ---")
    
    # 1. Check Recursion Depth
    print(f"Default Recursion Limit: {sys.getrecursionlimit()}")
    
    # 2. Optimization using Memoization
    from functools import lru_cache
    
    @lru_cache(maxsize=None)
    def fib_optimized(n):
        if n <= 1:
            return n
        return fib_optimized(n-1) + fib_optimized(n-2)
        
    print(f"Optimized Fibonacci (40th Value): {fib_optimized(40)}")
    print("Optimization: lru_cache caches results to prevent redundant calculations.")

def main():
    print("🚀 Python Recursion and Lambda Functions Practice")
    
    # 1. Factorial
    res_f = explain_recursion_factorial(5)
    print(f"Factorial of 5: {res_f}")
    
    # 2. Fibonacci
    res_fib = fibonacci_with_recursion(10)
    print(f"10th Fibonacci value: {res_fib}")
    
    # 3. Summing list
    res_sum = recursive_sum([10, 20, 30])
    print(f"Recursive sum of [10, 20, 30]: {res_sum}")
    
    # 4. Lambda and Higher-Order
    explain_lambda_functions()
    higher_order_functions()
    
    # 5. Advanced Optimization
    solve_interview_scenarios()

if __name__ == "__main__":
    main()

"""
Input/Output Examples:
Output:
Factorial of 5: 120
10th Fibonacci value: 55
Recursive sum of [10, 20, 30]: 60
...
map result  (Doubled): [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
...
Sorted words (Custom Key): ['apple', 'banana', 'Cherry', 'Kiwi']
...
Optimized Fibonacci (40th Value): 102334155
"""
