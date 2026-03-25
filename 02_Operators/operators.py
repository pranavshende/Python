"""
📁 02_Operators/operators.py
🧠 Topic: Python Operators (Comprehensive Guide)

Key Concepts Covered:
1. Arithmetic Operators
2. Relational (Comparison) Operators
3. Logical (AND, OR, NOT)
4. Bitwise (Shifting, AND, OR, XOR)
5. Assignment and Identity (is)
6. Membership (in)

Interview Focus:
- Is '==' same as 'is' in Python? (Crucial Question)
- Logic behind bitwise operations.
- Order of precedence (BODMAS for Python).
- Boolean short-circuiting.
"""

def demonstrate_arithmetic():
    """Shows all standard math operators."""
    print("\n--- Arithmetic Operators ---")
    
    a, b = 10, 3
    print(f"Addition (10 + 3): {a + b}")
    print(f"Subtraction (10 - 3): {a - b}")
    print(f"Multiplication (10 * 3): {a * b}")
    print(f"Division (10 / 3): {a / b} (Always returns float in Python 3)")
    print(f"Modulus (10 % 3): {a % b} (Remainder)")
    print(f"Exponentiation (10 ** 3): {a ** b} (Power of 3)")
    print(f"Floor Division (10 // 3): {a // b} (Removes decimal part)")

def demonstrate_relational_logical():
    """Comparison and logical reasoning."""
    print("\n--- Relational and Logical Operators ---")
    
    x, y, z = 5, 10, 5
    
    # Relational
    print(f"{x} == {y}? {x == y}")
    print(f"{x} == {z}? {x == z}")
    print(f"{x} != {y}? {x != y}")
    print(f"{x} > {y}? {x > y}")
    
    # Logical
    print(f"({x} < {y}) and ({x} == {z})? {(x < y) and (x == z)}")
    print(f"(5 > 10) or (10 > 5)? {(x > y) or (y > x)}")
    print(f"not (True)? {not True}")

def demonstrate_bitwise():
    """Low-level manipulation of data."""
    print("\n--- Bitwise Operators ---")
    
    a, b = 5, 3 # a=101, b=011
    
    print(f"5 & 3 (AND): {a & b} (001)")
    print(f"5 | 3 (OR): {a | b} (111)")
    print(f"5 ^ 3 (XOR): {a ^ b} (110)")
    print(f"~5 (Complement): {~a} (-(n+1))")
    print(f"5 << 1 (Left Shift): {a << 1} (1010 = 10)")
    print(f"5 >> 1 (Right Shift): {a >> 1} (010 = 2)")

def solve_identity_membership():
    """Distinction between object identity and list membership."""
    print("\n--- Identity (is) vs Equality (==) ---")
    
    L1 = [1, 2, 3]
    L2 = [1, 2, 3]
    L3 = L1
    
    print(f"L1 == L2: {L1 == L2} (Values are same)")
    # 'is' checks memory location (id)
    print(f"L1 is L2: {L1 is L2} (Different objects in memory)")
    print(f"L1 is L3: {L1 is L3} (Same memory address)")
    
    print("\n--- Membership Operators (in) ---")
    fruits = ["apple", "banana", "cherry"]
    print(f"Is 'apple' in fruits? {'apple' in fruits}")
    print(f"Is 'grapes' not in fruits? {'grapes' not in fruits}")

def solve_interview_question():
    """Scenario: Operator Precedence Calculation."""
    print("\n--- Interview Scenario: Operator Precedence ---")
    
    # 2 + 3 * 5 / 5 - 2 ** 3
    # Exponentiation (**) -> Multiplication (*) and Division (/) -> Add/Sub
    # 2 + 15 / 5 - 8 -> 2 + 3 - 8 -> -3
    
    expression = 2 + 3 * 5 / 5 - 2 ** 3
    print(f"Calculation of '2 + 3 * 5 / 5 - 2 ** 3' equals: {expression}")

def main():
    print("🚀 Python Operators Practice")
    demonstrate_arithmetic()
    demonstrate_relational_logical()
    demonstrate_bitwise()
    solve_identity_membership()
    solve_interview_question()

if __name__ == "__main__":
    main()

"""
Input/Output Examples:
Output:
Floor Division (10 // 3): 3
...
L1 == L2: True
L1 is L2: False (Crucial interview detail: 'is' checks id())
...
Calculation of '2 + 3 * 5 / 5 - 2 ** 3' equals: -3.0
"""
