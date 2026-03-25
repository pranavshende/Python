"""
📁 14_OOP/inheritance_polymorphism.py
🧠 Topic: Python Inheritance and Polymorphism

Key Concepts Covered:
1. Inheritance (Single, Multiple, Multilevel)
2. Base Class vs Derived Class
3. Method Overriding (Changing behavior in children)
4. Standard Method vs Static Method vs Class Method
5. Super() function (Calling parent attributes/methods)
6. Polymorphism (Multiple forms for a single object)

Interview Focus:
- Why use inheritance? (Code reuse, DRY principle)
- Difference between @staticmethod and @classmethod? (Instance vs Class data)
- How to solve Diamond Problem in multiple inheritance? (MRO lookup order)
- What is Method Overriding vs Overloading? (Python supports overriding, not overloading)
"""

# 1. Base Class (Parent)
class Animal:
    def __init__(self, name):
        self.name = name
        
    def speak(self):
        """ Abstract behavior to be implemented by children. """
        pass

# 2. Single Inheritance
class Dog(Animal):
    def speak(self):
        return f"{self.name} says WOOF!"

# 3. Multilevel Inheritance (Animal -> Mammal -> Whale)
class Mammal(Animal):
    def move(self):
        return "Moving like a Mammal..."

class Whale(Mammal):
    def move(self):
        return f"{self.name} is swimming (Multilevel)!"

# 4. Multiple Inheritance (Car and Electric mixins)
class Car:
    def fuel_type(self):
        return "Gasoline"

class Electric:
    def battery_type(self):
        return "Lithium-Ion"

class Tesla(Car, Electric): # Inheriting from TWO classes
    def fuel_type(self):
        return "Electricity (Multiple Inheritance)"

def explain_inheritance_types():
    """ Showing the hierarchy of inheritance in Python. """
    print("\n--- Testing Single and Multilevel Inheritance ---")
    
    # Single
    my_dog = Dog("Buddy")
    print(f"Dog Speak: {my_dog.speak()}")
    
    # Multilevel
    my_whale = Whale("Willy")
    print(f"Whale Move: {my_whale.move()}")
    
    # Multiple
    my_tesla = Tesla()
    print(f"Tesla Fuel: {my_tesla.fuel_type()}")
    print(f"Tesla Battery: {my_tesla.battery_type()}")

def explain_super_method():
    """ How to reach the parent from the child. """
    print("\n--- super() Function Usage ---")
    
    class Employee:
        def __init__(self, name, emp_id):
            self.name = name
            self.emp_id = emp_id
            
    class Developer(Employee):
        def __init__(self, name, emp_id, tech_stack):
            # Using super() to initialize parent attributes
            super().__init__(name, emp_id)
            self.tech_stack = tech_stack
            
    dev = Developer("Pranav", 101, "Python")
    print(f"Dev: {dev.name} (id: {dev.emp_id}) works on {dev.tech_stack}")

def demonstrate_polymorphism():
    """ One interface, many forms. """
    print("\n--- Polymorphism (Interface-like behavior) ---")
    
    class Cat(Animal):
        def speak(self):
            return f"{self.name} says MEOW!"
            
    animals = [Dog("Buddy"), Cat("Whiskers"), Dog("Rex")]
    
    for a in animals:
        # One call 'speak()' performs differently for each object
        print(f"Polymorphic Call: {a.speak()}")

class Utility:
    """ Static vs Class methods. """
    
    prefix = "[LOG]"
    
    @staticmethod
    def add_numbers(a, b): # Static methods don't need 'self' or 'cls'
        return a + b
        
    @classmethod
    def logger(cls, msg): # Class methods get 'cls' (reference to class)
        print(f"{cls.prefix}: {msg}")

def explain_method_types():
    print("\n--- Static vs Class Methods ---")
    
    # Static call
    res = Utility.add_numbers(10, 20)
    print(f"Static method add: {res}")
    
    # Class call
    Utility.logger("Testing polymorphism file...")

def main():
    print("🚀 Python OOP: Inheritance and Polymorphism Practice")
    explain_inheritance_types()
    explain_super_method()
    demonstrate_polymorphism()
    explain_method_types()

if __name__ == "__main__":
    main()

"""
Input/Output Examples:
Output:
Dog Speak: Buddy says WOOF!
Whale Move: Willy is swimming (Multilevel)!
...
Dev: Pranav (id: 101) works on Python
...
Polymorphic Call: Buddy says WOOF!
Polymorphic Call: Whiskers says MEOW!
...
Static method add: 30
[LOG]: Testing polymorphism file...
"""
