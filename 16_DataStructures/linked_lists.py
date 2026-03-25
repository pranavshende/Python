"""
📁 16_DataStructures/linked_lists.py
🧠 Topic: Python Data Structures (Singly Linked List)

Key Concepts Covered:
1. Node Class (Data and Next pointer)
2. Linked List Class (Head reference)
3. Operations: Append, Insert, Delete, Print
4. Traversing the list
5. Memory model: Pointers vs Continuous Arrays

Interview Focus:
- Why use a Linked List over a standard List (Array)? (O(1) insertion/deletion at head)
- Time Complexity of searching? (O(N))
- Difference between Singly and Doubly Linked List? (One vs Two pointers)
- Challenge: How to reverse a Linked List? (In-place swap)
"""

class Node:
    """ Each element (Node) contains its data and a reference to the next Node. """
    def __init__(self, data):
        self.data = data
        self.next = None

class SinglyLinkedList:
    """ Manager class for linked nodes. """
    def __init__(self):
        self.head = None # Initially empty
        
    def append(self, data):
        """ Add element to the END of the list. """
        new_node = Node(data)
        
        # 1. If list is empty, new node becomes the head
        if not self.head:
            self.head = new_node
            return
            
        # 2. Traverse to the last node
        last = self.head
        while last.next:
            last = last.next
            
        # 3. Point last node's next to the new node
        last.next = new_node
        
    def prepend(self, data):
        """ Add element to the START (Head) of the list. """
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node
        
    def delete(self, target_data):
        """ Remove first occurrence of data. """
        current = self.head
        
        # 1. If head is the target
        if current and current.data == target_data:
            self.head = current.next
            current = None
            return
            
        # 2. Search for the node and keep track of previous
        prev = None
        while current and current.data != target_data:
            prev = current
            current = current.next
            
        # 3. If missing, do nothing
        if not current:
            print(f"ERROR: Data '{target_data}' not found!")
            return
            
        # 4. Unlink the node from the chain
        prev.next = current.next
        current = None

    def reverse(self):
        """ In-place reversal of the list (Advanced Interview Prep). """
        prev = None
        current = self.head
        
        while current:
            next_node = current.next # Remember the rest of the list
            current.next = prev      # Point current node backwards
            prev = current           # Move 'prev' one step forward
            current = next_node      # Move 'current' one step forward
            
        self.head = prev # New head is the last node

    def display(self):
        """ Print the entire list structure. """
        elements = []
        current = self.head
        while current:
            elements.append(str(current.data))
            current = current.next
        print(" -> ".join(elements) + " -> [None]")

def main():
    print("🚀 Python Data Structures: Singly Linked List Practice")
    
    sll = SinglyLinkedList()
    
    # 1. Appending elements
    print("\n--- Appending 1, 2, 3 ---")
    sll.append(1)
    sll.append(2)
    sll.append(3)
    sll.display()
    
    # 2. Prepending (Adding to head)
    print("\n--- Prepending 0 ---")
    sll.prepend(0)
    sll.display()
    
    # 3. Deleting an element
    print("\n--- Deleting 2 ---")
    sll.delete(2)
    sll.display()
    
    # 4. Reversing the list
    print("\n--- Reversing the Linked List ---")
    sll.reverse()
    sll.display()

if __name__ == "__main__":
    main()

"""
Input/Output Examples:
Output:
1 -> 2 -> 3 -> [None]
...
0 -> 1 -> 2 -> 3 -> [None]
...
0 -> 1 -> 3 -> [None]
...
3 -> 1 -> 0 -> [None]
"""
