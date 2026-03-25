"""
📁 23_Testing/unit_testing.py
🧠 Topic: Python Testing and Debugging (unittest module)

Key Concepts Covered:
1. Unit Tests (Function tests)
2. Assertions (assertEqual, assertTrue, assertRaises)
3. TestCase class (unittest.TestCase)
4. Setup and Teardown methods (Resource management)
5. Running tests (unittest.main())
6. Mocking basics (unittest.mock)

Interview Focus:
- Why test code? (Regression testing, reliability, bug reduction)
- What is a Test Case? (Smallest unit of testing)
- Purpose of setUp() and tearDown()? (Initialize and clean up resources per test)
- Difference between assertEqual and assertTrue? (Value vs Logic check)
- How to test for specific errors (assertRaises)?
"""

import unittest

# 1. LOGIC: Sample code to test
def add_logic(a, b):
    return a + b

def divide_logic(a, b):
    if b == 0:
        raise ValueError("Denominator cannot be 0")
    return a / b

# 2. TESTING: Create a subclass of unittest.TestCase
class MyMathTests(unittest.TestCase):
    """ Suite for testing our arithmetic logic. """

    # 3. FIXTURES: Setup and TearDown
    def setUp(self):
        """ Runs before EVERY test. Initialize resources here. """
        self.val_a = 10
        self.val_b = 20
        print("SETTING UP: Preparing variables for testing...")
        
    def tearDown(self):
        """ Runs after EVERY test. Cleanup resources here. """
        print("TEAR DOWN: Cleaning up environment...")

    # 4. TEST CASES: Naming must start with 'test_'
    
    def test_addition_success(self):
        """ Positive test case for addition. """
        result = add_logic(self.val_a, self.val_b)
        self.assertEqual(result, 30, "The sum of 10 and 20 should be 30!")
        
    def test_division_success(self):
        """ Positive test case for division. """
        result = divide_logic(self.val_b, self.val_a)
        self.assertEqual(result, 2.0)
        
    def test_division_by_zero(self):
        """ Error check test case using assertRaises. """
        # Goal: Verify the function properly raises ValueError when b=0
        with self.assertRaises(ValueError):
            divide_logic(10, 0)
            
    def test_complex_assertion(self):
        """ Logic check using assertTrue. """
        self.assertTrue(add_logic(10, 5) > 10)

def main():
    """ 
    Execution logic for tests. 
    Use 'python unit_testing.py' to run it.
    """
    print("🚀 Running Unit Tests Practice...")
    
    # Executing the test runner
    # verbosity=2 provides extra details for each case
    unittest.main(argv=['first-arg-is-ignored'], exit=False, verbosity=2)

if __name__ == "__main__":
    main()

"""
Input/Output Examples:
Output:
Running Unit Tests Practice...
test_addition_success ... ok
test_division_by_zero ... ok
test_division_success ... ok
...
Ran 4 tests in 0.001s
OK
...
"""
