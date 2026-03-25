"""
📁 12_FileHandling/file_ops.py
🧠 Topic: Python File Operations (Read, Write, Append, and Binary)

Key Concepts Covered:
1. Open modes ('r', 'w', 'a', 'b')
2. The 'with' statement (Context Manager magic)
3. Reading content (read(), readline(), readlines())
4. Writing and Appending data
5. Binary file manipulation (rb, wb)
6. Cleaning up files using os.remove

Interview Focus:
- Why use the 'with' statement? (Auto-close, resource management)
- Difference between 'w' and 'a'? (Overwrite vs Append)
- How to read a large file without crashing RAM? (Line-by-line using for-loop)
- Difference between text and binary files.
"""

import os

FILE_NAME = "example_text.txt"
BINARY_FILE = "data_test.bin"

def basic_file_writing():
    """Writing to a text file (Overwrites existing)."""
    print("\n--- Basic File Writing ('w') ---")
    
    # 1. Open for writing (w)
    # Using 'with' is best practice to ensure file is closed correctly
    with open(FILE_NAME, "w") as f:
        f.write("Hello Python Course!\n")
        f.write("Line 2: File Handling is critical.\n")
        f.write("Line 3: Writing data to disk completed.\n")
    
    print(f"File '{FILE_NAME}' successfully written.")

def basic_file_reading():
    """Reading different formats from a file."""
    print("\n--- Basic File Reading ('r') ---")
    
    # 1. Reading entire content using .read()
    with open(FILE_NAME, "r") as f:
        print("Reading entire file content:")
        content = f.read()
        print(content)
        
    # 2. Reading line-by-line using .readline()
    with open(FILE_NAME, "r") as f:
        print("Reading line 1:")
        print(f.readline().strip())
        
    # 3. Reading all lines into a LIST using .readlines()
    with open(FILE_NAME, "r") as f:
        lines = f.readlines()
        print(f"Reading all lines into list: {lines}")

def optimized_large_file_read():
    """Efficiently reading large files."""
    print("\n--- Optimized Large File Reading ---")
    
    # Use for-loop on the file object itself (Memory efficient)
    with open(FILE_NAME, "r") as f:
        print("Line-by-line iteration:")
        for index, line in enumerate(f, start=1):
            print(f"L{index}: {line.strip()}")

def basic_file_appending():
    """Appending new content without losing previous data."""
    print("\n--- File Appending ('a') ---")
    
    with open(FILE_NAME, "a") as f:
        f.write("Line 4: This is an appended line.\n")
    
    print(f"New data appended to '{FILE_NAME}'. Verify with read.")

def binary_file_operations():
    """Handling non-text data (e.g., images, binary records)."""
    print("\n--- Binary File Operations ('rb', 'wb') ---")
    
    data_to_write = [10, 20, 30, 40]
    byte_array = bytes(data_to_write)
    
    # 1. Write binary
    with open(BINARY_FILE, "wb") as f:
        f.write(byte_array)
        
    print(f"Binary data {data_to_write} written to {BINARY_FILE}")
    
    # 2. Read binary
    with open(BINARY_FILE, "rb") as f:
        read_bytes = f.read()
        print(f"Binary data read: {list(read_bytes)}")

def cleanup_files():
    """Deleting the experimental files."""
    print("\n--- File Cleanup ---")
    
    for filename in [FILE_NAME, BINARY_FILE]:
        if os.path.exists(filename):
            os.remove(filename)
            print(f"Removed temporary file: {filename}")

def main():
    print("🚀 Python File Handling Practice")
    try:
        basic_file_writing()
        basic_file_reading()
        optimized_large_file_read()
        basic_file_appending()
        binary_file_operations()
    finally:
        cleanup_files()

if __name__ == "__main__":
    main()

"""
Input/Output Examples:
Output:
File 'example_text.txt' successfully written.
--- Basic File Reading ('r') ---
Reading entire file content:
Hello Python Course!
...
Binary data read: [10, 20, 30, 40]
Removed temporary file: example_text.txt
"""
