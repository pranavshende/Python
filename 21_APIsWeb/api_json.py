"""
📁 21_APIsWeb/api_json.py
🧠 Topic: Python APIs and Web (Requests module, JSON, and REST)

Key Concepts Covered:
1. JSON Serialization (json.dumps)
2. JSON Deserialization (json.loads)
3. HTTP Requests (GET, POST, PUT, DELETE)
4. Query Parameters and Headers
5. Handling JSON responses
6. API Authentication basics

Interview Focus:
- Difference between json.loads and json.load? (String vs File)
- What is serialization? (Converting data structure to JSON string)
- Difference between GET and POST requests? (Data retrieval vs Submission)
- Why use the 'requests' library instead of 'urllib'? (Simplicity, readability)
- Common HTTP status codes (200, 201, 400, 401, 404, 500)
"""

import json
import requests

def demonstrate_json_handling():
    """ 
    Converting Python objects to JSON and back. 
    Serialization: python -> json
    Deserialization: json -> python
    """
    print("\n--- JSON Serialization & Deserialization ---")
    
    # 1. Python Dictionary (Data Structure)
    data = {
        "id": 101,
        "username": "alice_dev",
        "roles": ["admin", "developer"],
        "active": True
    }
    
    # SERIALIZATION (dumps: dump string)
    json_string = json.dumps(data, indent=4)
    print(f"Serialized JSON (Type: {type(json_string).__name__}):\n{json_string}")
    
    # DESERIALIZATION (loads: load string)
    parsed_data = json.loads(json_string)
    print(f"Deserialized User: {parsed_data['username']} (Roles: {parsed_data['roles']})")

def demonstrate_api_requests():
    """ 
    Using 'requests' to interact with remote REST APIs. 
    Example API: {JSON} Placeholder (Free fake API)
    """
    print("\n--- REST API with 'requests' (GET Request) ---")
    
    URL = "https://jsonplaceholder.typicode.com/posts/1"
    
    try:
        # 1. GET Request
        response = requests.get(URL, timeout=5)
        
        # 2. Check status (200 OK)
        if response.status_code == 200:
            print("Successfully fetched data from Public API!")
            
            # 3. Parse JSON response directly
            post_data = response.json()
            print(f"Post Title: {post_data['title']}")
            print(f"Post Body:  {post_data['body'][:50]}...")
            
        else:
            print(f"Request failed with status: {response.status_code}")
            
    except requests.exceptions.RequestException as e:
        print(f"API ERROR: {e}")

def demonstrate_post_request():
    """ Sending data to a server using POST. """
    print("\n--- REST API (POST Request) ---")
    
    URL = "https://jsonplaceholder.typicode.com/posts"
    new_post = {
        "title": "Learning Python API",
        "body": "This is a test post sent via requests.",
        "userId": 1
    }
    
    headers = {"Content-type": "application/json; charset=UTF-8"}
    
    try:
        # POST: creating a new resource
        # json= argument automatically handles serialization
        response = requests.post(URL, json=new_post, headers=headers)
        
        if response.status_code == 201: # 201 Created
            print("Successfully CREATED new resource!")
            print(f"Response data: {response.json()}")
    except Exception as e:
        print(f"POST ERROR: {e}")

def main():
    print("🚀 Python APIs and Web Practice")
    demonstrate_json_handling()
    # Note: Requires internet connection to run API examples
    demonstrate_api_requests()
    demonstrate_post_request()

if __name__ == "__main__":
    main()

"""
Input/Output Examples:
Output:
Serialized JSON (Type: str): { "id": 101, ... }
Deserialized User: alice_dev
...
API with 'requests' (GET Request)
Successfully fetched data from Public API!
Post Title: sunt aut facere repellat provident occaecati excepturi optio reprehenderit
...
"""
