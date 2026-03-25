"""
📁 05_Strings/string_methods.py
🧠 Topic: Common String Methods (Comprehensive Guide)

Key Concepts Covered:
1. Case Methods (upper, lower, capitalize, title)
2. Search Methods (find, count, index, replace)
3. Validation Methods (isdigit, isalpha, isalnum)
4. Formatting Methods (strip, split, join)
5. Encoding and Decoding (UTF-8, ASCII)

Interview Focus:
- What's the difference between find() and index()? (Error handling)
- How to remove leading and trailing whitespaces? (.strip())
- Best way to join strings from a list into a single sentence? (.join())
"""

def case_methods():
    """Modifying cases for strings."""
    print("\n--- String Case Methods ---")
    
    text = "pYtHoN iS aWeSoMe"
    
    print(f"Original: {text}")
    print(f"Upper:    {text.upper()}")
    print(f"Lower:    {text.lower()}")
    print(f"Capitalize: {text.capitalize()}") # First letter of first word
    print(f"Title:    {text.title()}") # First letter of EVERY word
    print(f"Swap Case: {text.swapcase()}")

def search_replace_methods():
    """Finding and modifying sub-strings."""
    print("\n--- Searching and Replacing ---")
    
    msg = "Python is great. Python is fast."
    
    # 1. find vs index
    print(f"find('Python'): {msg.find('Python')}") # 0
    print(f"find('Java'):   {msg.find('Java')}")   # -1 (NOT FOUND)
    
    try:
        print(f"index('Java'):  {msg.index('Java')}") # Raises ValueError
    except ValueError as e:
        print(f"index('Java'): Caught ERROR: {e}")
        
    # 2. count
    print(f"count('Python'): {msg.count('Python')}")
    
    # 3. replace (Returns a NEW string, does not modify original)
    print(f"replace('great', 'awesome'): {msg.replace('great', 'awesome')}")

def validation_methods():
    """Checking string contents."""
    print("\n--- Validation and Content Checks ---")
    
    s1, s2, s3 = "123", "ABC", "Python3"
    
    print(f"'{s1}' is Digit: {s1.isdigit()}")
    print(f"'{s2}' is Alpha: {s2.isalpha()}")
    print(f"'{s3}' is Alnum: {s3.isalnum()}")
    
    # startsWith and endsWith
    email = "test@example.com"
    print(f"Email ends with '.com'? {email.endswith('.com')}")
    print(f"Email starts with 'test'? {email.startswith('test')}")

def strip_split_join():
    """Essential methods for text processing."""
    print("\n--- Stripping, Splitting, and Joining ---")
    
    # strip: remove extra characters from ends
    noisy_text = "   User Name   "
    print(f"Cleaned: '{noisy_text.strip()}'")
    
    # split: convert string to list based on delimiter
    data = "apple,banana,cherry"
    fruit_list = data.split(",")
    print(f"Split List: {fruit_list}")
    
    # join: convert list to string with delimiter
    joined_text = " | ".join(fruit_list)
    print(f"Joined String: {joined_text}")

def solve_interview_question():
    """Scenario: How to check if a string is a palindrome?"""
    print("\n--- Scenario: Check for Palindrome ---")
    
    # Simple check for case-insensitive palindrome
    def is_palindrome(s):
        clean_s = "".join(char.lower() for char in s if char.isalnum())
        return clean_s == clean_s[::-1]
    
    test_str = "A man, a plan, a canal: Panama"
    print(f"Is '{test_str}' a palindrome? {is_palindrome(test_str)}")

def main():
    print("🚀 Python String Methods Practice")
    case_methods()
    search_replace_methods()
    validation_methods()
    strip_split_join()
    solve_interview_question()

if __name__ == "__main__":
    main()

"""
Input/Output Examples:
Output:
capitalize: Python is awesome
...
find('Java'): -1
index('Java'): Caught ERROR: substring not found
...
Split List: ['apple', 'banana', 'cherry']
Joined String: apple | banana | cherry
...
Is 'A man, a plan, a canal: Panama' a palindrome? True
"""
