"""
📁 18_RegEx/regex_basics.py
🧠 Topic: Python Regular Expressions (re module)

Key Concepts Covered:
1. Pattern Matching (search, match, findall)
2. Metacharacters (. ^ $ * + ? {} [] \ | ())
3. Quantifiers and Qualifiers
4. Special Sequences (\d, \w, \s)
5. Practical examples: Email and Date validation

Interview Focus:
- Difference between re.match() and re.search()? (Match: start only, Search: anywhere)
- What is a raw string (r"")? (Prevents backslash escaping)
- How to extract only numbers from a mixed string? (\d+)
- Use of flags like re.IGNORECASE.
"""

import re

def basic_matching_patterns():
    """ Using re.search() and re.match(). """
    print("\n--- Basic Pattern Matching (Search vs Match) ---")
    
    text = "The Python 3.10 is great."
    
    # 1. match() matches ONLY from the start of the string
    res_match = re.match(r"Python", text)
    print(f"Match 'Python': {res_match} (Match must start at index 0)")
    
    # 2. search() matches ANYWHERE in the string
    res_search = re.search(r"Python", text)
    print(f"Search 'Python': {res_search} (Span: {res_search.span()})")
    
    # 3. IGNORECASE flag
    res_ignore = re.search(r"python", text, re.I)
    print(f"Case-insensitive Search: {res_ignore}")

def common_metacharacters():
    """ Regex character classes and ranges. """
    print("\n--- RegEx Metacharacters & Sequences ---")
    
    text = "User_123, Admin_456, Ghost_789"
    
    # \d+ : match one or more digits
    digits = re.findall(r"\d+", text)
    print(f"Digits found: {digits}")
    
    # [A-Z]+ : match one or more uppercase letters
    upper = re.findall(r"[A-Z]+", text)
    print(f"Uppercase letters: {upper}")
    
    # Subtraction/Substitution
    # re.sub(pattern, replacement, text)
    new_text = re.sub(r"\d+", "HIDDEN", text)
    print(f"Masked Text: {new_text}")

def advanced_validation_logic():
    """ Real-world data validation: Emails and Dates. """
    print("\n--- Practical Scenario: Email Validation ---")
    
    emails = ["test@example.com", "invalid-email@", "alice123@domain.org"]
    # regex: [anything] @ [domain] . [extension]
    email_pattern = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"
    
    for email in emails:
        if re.match(email_pattern, email):
            print(f"VALID:   {email}")
        else:
            print(f"INVALID: {email}")

def capture_groups_logic():
    """ Grouping results via parentheses (). """
    print("\n--- Capture Groups and Groups Management ---")
    
    # Goal: Extract date: DD-MM-YYYY
    text = "Order placed on 25-12-2024"
    date_pattern = r"(\d{2})-(\d{2})-(\d{4})" # 3 groups: Day, Month, Year
    
    match = re.search(date_pattern, text)
    if match:
        print(f"Full Date: {match.group(0)}")
        print(f"Day:       {match.group(1)}")
        print(f"Month:     {match.group(2)}")
        print(f"Year:      {match.group(3)}")

def main():
    print("🚀 Python Regular Expressions Practice")
    basic_matching_patterns()
    common_metacharacters()
    advanced_validation_logic()
    capture_groups_logic()

if __name__ == "__main__":
    main()

"""
Input/Output Examples:
Output:
Match 'Python': None
Search 'Python': <re.Match object; span=(4, 10), match='Python'>
...
Digits found: ['123', '456', '789']
Masked Text: User_HIDDEN, Admin_HIDDEN, Ghost_HIDDEN
...
Full Date: 25-12-2024
Day:       25
...
"""
