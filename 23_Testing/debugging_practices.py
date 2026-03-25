"""
📁 23_Testing/debugging_practices.py
🧠 Topic: Python Debugging (pdb module and logging module)

Key Concepts Covered:
1. The Python Debugger (pdb)
2. Interactive Breakpoints (set_trace, breakpoint())
3. Stepping through code (n, s, c, l)
4. Logging levels (DEBUG, INFO, WARNING, ERROR, CRITICAL)
5. Logging to file and console
6. Formatting logs

Interview Focus:
- Why use logging over print()? (Persistence, severity levels, configuration)
- Basic pdb commands: What's the difference between 'next' and 'step'? (Step: enters functions)
- How to set a breakpoint at a specific line? (breakpoint() in Python 3.7+)
- Significance of log rotation? (Preventing disk fill)
"""

import pdb
import logging

# 1. LOGGING CONFIGURE: Best for production tracing
# Level: DEBUG (Lowest) -> INFO -> WARNING -> ERROR -> CRITICAL (Highest)
logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s | %(levelname)-8s | %(message)s',
    filename='app_trace.log', # Logging to a file for persistence
    filemode='w'
)

# Also adding a console handler to see logs locally
console = logging.StreamHandler()
console.setLevel(logging.INFO)
formatter = logging.Formatter('%(levelname)s: %(message)s')
console.setFormatter(formatter)
logging.getLogger('').addHandler(console)

def logic_with_errors(a, b):
    """ Demonstrating pdb and logging for debugging. """
    logging.info(f"Adding {a} and {b}...")
    
    # 1. pdb (Interactive Debugging)
    # Uncomment the next line to enter interactive debug mode!
    # breakpoint() # equivalent to import pdb; pdb.set_trace()
    
    # Simulate a calculation but log if it looks strange
    result = a + b
    
    if result < 0:
        logging.warning("Calculation result is negative! Is this expected?")
        
    logging.info(f"Success. Result: {result}")
    return result

def solve_division_bug(a, b):
    """ Using logging for error tracking instead of simple print. """
    try:
        res = a / b
        logging.debug(f"Division {a}/{b} = {res}")
        return res
    except ZeroDivisionError:
        logging.error(f"Division Error: Cannot divide {a} by 0!")
        return None

def main():
    print("🚀 Python Debugging Practice (Check 'app_trace.log' for details)")
    
    # 1. Run basic logic
    logic_with_errors(10, 20)
    logic_with_errors(10, -50) # Will trigger a WARNING
    
    # 2. Run division logic
    solve_division_bug(100, 5)
    solve_division_bug(100, 0) # Will trigger an ERROR
    
    # 3. Informing user about the log file
    with open('app_trace.log', 'r') as f:
        print("\n--- Recent Log Entries ---")
        print(f.read())

if __name__ == "__main__":
    main()

"""
Input/Output Examples:
Output:
INFO: Adding 10 and 20...
INFO: Success. Result: 30
...
WARNING: Calculation result is negative! Is this expected?
...
ERROR: Division Error: Cannot divide 100 by 0!
...
"""
