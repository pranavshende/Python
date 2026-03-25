"""
📁 14_OOP/encapsulation_abstraction.py
🧠 Topic: Python OOP Advanced (Encapsulation and Abstraction)

Key Concepts Covered:
1. Encapsulation (Private vs Protected attributes)
2. Name Mangling (__attribute_name)
3. Getters and Setters (@property decorator)
4. Abstraction (Using abc module)
5. Abstract Base Classes (ABC)
6. Abstract Methods (@abstractmethod)

Interview Focus:
- Does Python have 'private' keywords? (No, only naming conventions: _ and __)
- What is name mangling? (Preventing attribute access by external classes)
- Why use abstraction? (Define a common structure for children)
- Difference between @property and a simple method? (Syntactic sugar for getters)
"""

from abc import ABC, abstractmethod

# 1. ENCAPSULATION (Hiding internal state)
class Account:
    def __init__(self, owner, balance):
        self.owner = owner     # PUBLIC attribute
        self._id = 101         # PROTECTED attribute (convension: _ prefix)
        self.__balance = balance # PRIVATE attribute (convension: __ prefix)
        
    # Getter: Using @property decorator to access private data
    @property
    def balance(self):
        return f"Current Balance: ${self.__balance}"
    
    # Setter: Using @balance.setter to update private data with logic
    @balance.setter
    def balance(self, amount):
        if amount >= 0:
            self.__balance = amount
        else:
            print("ERROR: Invalid amount! Cannot set negative balance.")
            
    def __internal_log(self):
        """ Private method (accessible only inside this class). """
        print("Logging internal transaction record...")

def explain_encapsulation():
    """ Showing access control. """
    print("\n--- Testing Encapsulation and Access Control ---")
    
    acc = Account("Pranav", 5000)
    
    # 1. Public Access
    print(f"Owner: {acc.owner}")
    
    # 2. Protected Access (Possible but discouraged)
    print(f"Protected ID: {acc._id}")
    
    # 3. Private Access (Results in AttributeError)
    try:
        # print(f"Private balance: {acc.__balance}")
        print("Verification: Cannot access '__balance' directly.")
    except AttributeError:
        print("AttributeError caught: Private data is hidden.")
        
    # 4. Accessing private via Name Mangling (Discouraged)
    # Correct format: _ClassName__AttributeName
    print(f"Bypassing via Mangling: {acc._Account__balance}")
    
    # 5. Correct Access via Properties
    print(f"Accessing via Property: {acc.balance}")
    acc.balance = 6000 # Setter call
    print(f"Modified via Property: {acc.balance}")
    acc.balance = -100 # Setter logic check
    
# 2. ABSTRACTION (Defining a blueprint)
class Shape(ABC): # Inheriting from ABC (Abstract Base Class)
    @abstractmethod
    def area(self):
        """ Force child classes to implement 'area'. """
        pass
    
    @abstractmethod
    def perimeter(self):
        """ Force child classes to implement 'perimeter'. """
        pass

class Square(Shape):
    def __init__(self, side):
        self.side = side
        
    def area(self): # Required implementation
        return self.side * self.side
        
    def perimeter(self): # Required implementation
        return 4 * self.side

def explain_abstraction():
    """ Showing the enforcement of blueprints. """
    print("\n--- Testing Abstraction (ABC) ---")
    
    # 1. Attempt to instantiate an abstract class (Will FAIL)
    try:
        # s = Shape()
        print("Verification: Cannot instantiate Abstract Class 'Shape'.")
    except TypeError as e:
        print(f"Caught ERROR: {e}")
        
    # 2. Instantiate implementing class
    sq = Square(5)
    print(f"Square Area: {sq.area()}")
    print(f"Square Perimeter: {sq.perimeter()}")

def main():
    print("🚀 Python OOP: Encapsulation and Abstraction Practice")
    explain_encapsulation()
    explain_abstraction()

if __name__ == "__main__":
    main()

"""
Input/Output Examples:
Output:
Owner: Pranav
Verification: Cannot access '__balance' directly.
Bypassing via Mangling: 5000
Modified via Property: Current Balance: $6000
...
Verification: Cannot instantiate Abstract Class 'Shape'.
Square Area: 25
Square Perimeter: 20
"""
