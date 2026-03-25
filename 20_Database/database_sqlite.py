"""
📁 20_Database/database_sqlite.py
🧠 Topic: Python Database Connectivity (SQLite3)

Key Concepts Covered:
1. Connecting to Database (sqlite3.connect)
2. Cursor Object (Executing SQL commands)
3. CRUD Operations (Create, Read, Update, Delete)
4. Parameterized Queries (Preventing SQL Injection)
5. Fetching (fetchone, fetchall)
6. Transaction Management (commit, rollback)

Interview Focus:
- Why use SQLite? (File-based, serverless, great for testing/small apps)
- What is a Cursor? (Control structure for traversal over records)
- Why use '?' placeholders instead of string formatting? (SQL Injection protection)
- Difference between commit() and close()? (Saving vs Terminating)
"""

import sqlite3
import os

DB_NAME = "practice_db.sqlite"

def create_table(conn):
    """ Initialize a table for storing student records. """
    print("\n--- Creating Table 'Students' ---")
    cursor = conn.cursor()
    
    # 1. SQL Create Command
    query = \"\"\"
    CREATE TABLE IF NOT EXISTS Students (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        age INTEGER,
        grade TEXT
    )
    \"\"\"
    cursor.execute(query)
    conn.commit()
    print("Table ready.")

def insert_data(conn, name, age, grade):
    """ Demonstrate INSERT Operation with parameterization. """
    print(f"\n--- Inserting Record: {name} ---")
    cursor = conn.cursor()
    
    # Using '?' placeholders is CRITICAL for security
    query = "INSERT INTO Students (name, age, grade) VALUES (?, ?, ?)"
    cursor.execute(query, (name, age, grade))
    conn.commit()
    print("Insert successful.")

def read_data(conn):
    """ Demonstrate SELECT Operation and fetching results. """
    print("\n--- Reading All Student Records (SELECT) ---")
    cursor = conn.cursor()
    
    cursor.execute("SELECT * FROM Students")
    results = cursor.fetchall()
    
    for row in results:
        print(f"ID: {row[0]} | Name: {row[1]:10} | Age: {row[2]} | Grade: {row[3]}")

def update_data(conn, student_id, new_grade):
    """ Demonstrate UPDATE Operation. """
    print(f"\n--- Updating Student ID {student_id} to Grade {new_grade} ---")
    cursor = conn.cursor()
    
    query = "UPDATE Students SET grade = ? WHERE id = ?"
    cursor.execute(query, (new_grade, student_id))
    conn.commit()

def delete_data(conn, student_id):
    """ Demonstrate DELETE Operation. """
    print(f"\n--- Deleting Student ID {student_id} ---")
    cursor = conn.cursor()
    
    query = "DELETE FROM Students WHERE id = ?"
    cursor.execute(query, (student_id,))
    conn.commit()

def cleanup():
    """ Delete the actual database file after practice. """
    if os.path.exists(DB_NAME):
        os.remove(DB_NAME)
        print("\nPractice Database File removed.")

def main():
    print("🚀 Python Database (SQLite3) Practice")
    
    # 1. ESTABLISH CONNECTION
    try:
        connection = sqlite3.connect(DB_NAME)
        
        # 2. RUN CRUD OPERATIONS
        create_table(connection)
        
        insert_data(connection, "Alice", 20, "A")
        insert_data(connection, "Bob", 22, "B")
        insert_data(connection, "Charlie", 19, "C")
        
        read_data(connection)
        
        update_data(connection, 1, "A+")
        read_data(connection)
        
        delete_data(connection, 2)
        read_data(connection)
        
        # 3. CLOSE CONNECTION
        connection.close()
        print("\nDatabase connection closed.")
        
    except sqlite3.Error as e:
        print(f"DATABASE ERROR: {e}")
        
    finally:
        cleanup()

if __name__ == "__main__":
    main()

"""
Input/Output Examples:
Output:
Creating Table 'Students'
Table ready.
...
Insert successful.
...
ID: 1 | Name: Alice      | Age: 20 | Grade: A
ID: 2 | Name: Bob        | Age: 22 | Grade: B
...
Final Selection (Updated Table):
ID: 1 | Name: Alice      | Age: 20 | Grade: A+
ID: 3 | Name: Charlie    | Age: 19 | Grade: C
...
"""
