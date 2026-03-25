"""
📁 16_DataStructures/stacks_queues.py
🧠 Topic: Python Data Structures (Stacks and Queues)

Key Concepts Covered:
1. Stack (LIFO: Last In First Out)
2. Queue (FIFO: First In First Out)
3. Implementation via list (Simpler)
4. Implementation via collections.deque (Efficient)
5. Practical applications (Undo, Call stack, Order processing)

Interview Focus:
- Why is 'collections.deque' better than a list for queues? (O(1) pop(0) vs O(N))
- Difference between LIFO and FIFO.
- How to implement a stack using two queues? (Advanced)
- What is double-ended queue? (Deque)
"""

from collections import deque

def demonstrate_stack_operations():
    """ 
    LIFO Principle: Like a stack of plates. 
    Operations: push (append), pop.
    """
    print("\n--- Stack Implementation (LIFO) ---")
    
    # 1. Using a standard list (Efficient for stack)
    stack = []
    
    # Pushing elements
    stack.append("URL 1")
    stack.append("URL 2")
    stack.append("URL 3")
    print(f"Stack after push: {stack}")
    
    # Popping elements
    popped = stack.pop()
    print(f"Popped from stack: {popped}")
    print(f"Stack after pop:  {stack}")
    
    # Empty check and peek
    if stack:
        print(f"Peek (Top of stack): {stack[-1]}")

def demonstrate_queue_operations():
    """ 
    FIFO Principle: Like a line at a movie theater. 
    Operations: enqueue (append), dequeue (popleft).
    """
    print("\n--- Queue Implementation (FIFO) ---")
    
    # 1. Using collections.deque (Professional choice)
    queue = deque()
    
    # ENQUEUE (Add to back)
    queue.append("Customer 1")
    queue.append("Customer 2")
    queue.append("Customer 3")
    print(f"Queue after enqueue: {list(queue)}")
    
    # DEQUEUE (Remove from front)
    # deque.popleft() is O(1) performance!
    first = queue.popleft()
    print(f"First served: {first}")
    print(f"Queue after dequeue: {list(queue)}")
    
    # Status
    print(f"Remaining Customer Count: {len(queue)}")

def explain_undo_logic():
    """ Practical Scenario: Implementing a basic Undo manager. """
    print("\n--- Scenario: Undo Manager (using stack) ---")
    
    actions = ["Typing...", "Deleting...", "Highlighting..."]
    history = []
    
    for action in actions:
        print(f"Action: {action}")
        history.append(action)
        
    # Undo the last action
    if history:
        last = history.pop()
        print(f"UNDOING: {last}")
        print(f"Current History: {history}")

def explain_ticketing_system():
    """ Practical Scenario: Building a simple ticketing service. """
    print("\n--- Scenario: Support Ticket System (using queue) ---")
    
    tickets = deque(["Ticket #101: Login error", "Ticket #102: API failure"])
    print(f"Initial Tickets: {list(tickets)}")
    
    # New ticket arrives
    tickets.append("Ticket #103: Styling bug")
    
    # Serve one ticket
    served = tickets.popleft()
    print(f"SERVED: '{served}' Processing completed.")
    print(f"Queue status: {len(tickets)} pending.")

def main():
    print("🚀 Python Data Structures: Stacks and Queues Practice")
    demonstrate_stack_operations()
    demonstrate_queue_operations()
    explain_undo_logic()
    explain_ticketing_system()

if __name__ == "__main__":
    main()

"""
Input/Output Examples:
Output:
Stack after push: ['URL 1', 'URL 2', 'URL 3']
Popped from stack: URL 3
...
Queue after enqueue: ['Customer 1', 'Customer 2', 'Customer 3']
First served: Customer 1
...
UNDOING: Highlighting...
...
"""
