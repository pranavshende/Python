"""
📁 20_Database/database_mysql.py
🧠 Topic: Python Database Connectivity (MySQL)

Key Concepts Covered:
1. Connecting to MySQL (mysql.connector.connect)
2. Handling Database drivers (Install via pip)
3. MySQL CRUD operations
4. Difference between SQLite (local file) and MySQL (server-based)
5. Connection pooling basics

Interview Focus:
- Why use MySQL over SQLite? (Scaling, user concurrency, multi-server)
- How to store passwords securely? (Env variables, never hard-coded)
- What is a database driver? (The bridge between app and database engine)
- Handling ConnectionError scenarios.
"""

import os
# from mysql.connector import connect # Needs 'mysql-connector-python' installed

def demonstrate_mysql_connectivity():
    """ 
    Conceptual overview of using MySQL with Python. 
    Steps:
    1. pip install mysql-connector-python
    2. Import connect from mysql.connector
    3. Connect using Host, User, Password, and Database.
    """
    print("\n--- MySQL Connection Blueprint ---")
    
    # MOCKING the values for documentation
    host = "localhost"
    user = "root"
    password = "SECURE_PASSWORD" # Use environment variables instead!
    database = "practice_schema"
    
    print(f"Connection String: mysql.connector.connect(host='{host}', user='{user}', password='...', database='{database}')")
    
    # 2. Logic for CRUD in MySQL (Structure similar to SQLite)
    query = "SELECT * FROM Users WHERE id = %s" # MySQL uses %s instead of ? for binding
    print(f"Parameterized Query (MySQL): {query}")

def solve_env_best_practice():
    """ How to safely manage database credentials using OS ENV. """
    print("\n--- Best Practice: Environment Variables ---")
    
    # Attempt to read from environment (Safe approach)
    db_pass = os.environ.get("DB_PASSWORD", "NOT_SET")
    if db_pass == "NOT_SET":
        print("Advisory: Set 'DB_PASSWORD' in your OS to link correctly.")
    else:
        print("Success: Database password hidden from code and loaded correctly.")

def comparison_summary():
    """ SQLite vs MySQL (High-level). """
    print("\n--- DB Comparison Matrix ---")
    print("1. SQLite: Serverless, simple file, zero-config, best for development/lite apps.")
    print("2. MySQL: Server-based, concurrent users, scalable, best for production/web apps.")
    print("3. Driver: mysql-connector-python or PyMySQL is required for MySQL.")

def main():
    print("🚀 Python MySQL Connectivity Practice (Conceptual)")
    demonstrate_mysql_connectivity()
    solve_env_best_practice()
    comparison_summary()
    
    # Note: For actual running code, uncomment the import and connect calls 
    # after installing the connector library.

if __name__ == "__main__":
    main()

"""
Input/Output Examples:
Output:
MySQL Connection Blueprint
Connection String: mysql.connector.connect(host='localhost', ...)
...
Best Practice: Environment Variables
...
"""
