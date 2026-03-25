"""
📁 14_OOP/class_objects.py
🧠 Topic: Python OOP Basics (Classes, Objects, and Constructors)

Key Concepts Covered:
1. Class Definition (class)
2. Object Instantiation
3. The __init__ Method (Constructor)
4. Instance Attributes vs Class Attributes
5. Self keyword (Reference to current instance)
6. String Representation (__str__ and __repr__)

Interview Focus:
- Difference between a Class and an Object? (Blueprint vs Reality)
- Purpose of self? (Instance identity)
- Difference between a class attribute and an instance attribute? (Scope/Memory)
- What is __init__? (Constructor for object initialization)
"""

class Student:
    """ Basic Class Representation. """
    
    # CLASS ATTRIBUTES (Same for EVERY object created from this class)
    college = "Python Institute"
    student_count = 0
    
    def __init__(self, name, age, grade):
        # INSTANCE ATTRIBUTES (Unique to each object)
        self.name = name
        self.age = age
        self.grade = grade
        
        # Updating class attributes inside instance (use Student prefix or self)
        Student.student_count += 1
        
    def display_details(self):
        """ Basic instance method. """
        print(f"Student: {self.name} | Age: {self.age} | Grade: {self.grade} | {self.college}")

    # STRING REPRESENTATION (User friendly: For print())
    def __str__(self):
        return f"Student: {self.name}"
    
    # REPRESENTATION (Dev friendly: For debugging/logging)
    def __repr__(self):
        return f"Student(name='{self.name}', age={self.age}, grade='{self.grade}')"

def explain_class_vs_instance():
    """ Showing the distinction in memory. """
    print("\n--- Instance vs Class Attributes ---")
    
    s1 = Student("Alice", 20, "A")
    s2 = Student("Bob", 22, "B")
    
    # 1. Accessing instance data
    print(f"s1 Name: {s1.name}")
    print(f"s2 Name: {s2.name}")
    
    # 2. Accessing class data
    print(f"s1 College: {s1.college}")
    print(f"s2 College: {s2.college}")
    print(f"Total Students: {Student.student_count}")
    
    # 3. Modifying class data (Affects all instances)
    Student.college = "Advanced Python Academy"
    print(f"Updated College: {s1.college} (Reflection in s1)")

def explain_string_repr():
    """ User vs Dev representations. """
    print("\n--- String Representation (__str__ vs __repr__) ---")
    
    s = Student("Charlie", 19, "A")
    
    print(f"Str result:   {str(s)}")
    print(f"Repr result:  {repr(s)}")

def main():
    print("🚀 Python OOP: Classes and Objects Practice")
    explain_class_vs_instance()
    explain_string_repr()

if __name__ == "__main__":
    main()

"""
Input/Output Examples:
Output:
s1 Name: Alice
Total Students: 2
...
Updated College: Advanced Python Academy (Reflection in s1)
...
Str result:   Student: Charlie
Repr result:  Student(name='Charlie', age=19, grade='A')
"""
