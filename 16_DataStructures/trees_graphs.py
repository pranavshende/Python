"""
📁 16_DataStructures/trees_graphs.py
🧠 Topic: Python Data Structures (Binary Search Tree and Adjacency List Graph)

Key Concepts Covered:
1. Binary Search Tree (BST) Theory
2. BST Operations: Insert, Traverse (In-Order)
3. Graph Representation (Adjacency List using dict)
4. Graph Operations: Add Vertex, Add Edge, BFS/DFS Concepts
5. Time Complexity of searching in BST (O(log N))

Interview Focus:
- What is a Binary Search Tree? (Rule: Left < Parent < Right)
- Difference between Tree and Graph? (A tree is a connected graph without cycles)
- Benefits of a balanced BST? (Optimal searching performance)
- Difference between BFS (queue) and DFS (stack)?
"""

# --- 1. BINARY SEARCH TREE (BST) ---
class TreeNode:
    """ Node with left and right children. """
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

class BST:
    """ Manager for a collection of TreeNodes. """
    def __init__(self):
        self.root = None
        
    def insert(self, val):
        """ Add value into the BST following the hierarchy rules. """
        if not self.root:
            self.root = TreeNode(val)
        else:
            self._insert_recursive(self.root, val)
            
    def _insert_recursive(self, current, val):
        # 1. If value is LESS, go LEFT
        if val < current.val:
            if not current.left:
                current.left = TreeNode(val)
            else:
                self._insert_recursive(current.left, val)
        # 2. If value is GREATER, go RIGHT
        else:
            if not current.right:
                current.right = TreeNode(val)
            else:
                self._insert_recursive(current.right, val)
                
    def inorder_traversal(self, current, result=None):
        """ LEFT -> ROOT -> RIGHT (Returns values in SORTED order). """
        if result is None: result = []
        
        if current:
            self.inorder_traversal(current.left, result)
            result.append(current.val)
            self.inorder_traversal(current.right, result)
        return result

# --- 2. GRAPH REPRESENTATION (Adjacency List) ---
class Graph:
    """ Using a dictionary to map each vertex to its neighbors. """
    def __init__(self):
        self.adj_list = {}
        
    def add_vertex(self, v):
        """ Initialize new node in the graph. """
        if v not in self.adj_list:
            self.adj_list[v] = []
            
    def add_edge(self, v1, v2):
        """ Connect two nodes (Undirected graph). """
        if v1 in self.adj_list and v2 in self.adj_list:
            self.adj_list[v1].append(v2)
            self.adj_list[v2].append(v1)

    def display(self):
        """ Print the neighbor list for each vertex. """
        for v, neighbors in self.adj_list.items():
            print(f"Vertex {v}: {neighbors}")

def main():
    print("🚀 Python Data Structures: Trees and Graphs Practice")
    
    # 1. Testing BST
    print("\n--- Testing Binary Search Tree (BST) ---")
    bst = BST()
    values = [20, 10, 30, 5, 15]
    for v in values:
        bst.insert(v)
    
    # In-order of BST will always yield sorted values
    print(f"Inserted values: {values}")
    print(f"In-Order Traversal (Sorted result): {bst.inorder_traversal(bst.root)}")
    
    # 2. Testing Graph
    print("\n--- Testing Graph (Adjacency List) ---")
    g = Graph()
    
    # Creating vertices
    for char in ["A", "B", "C", "D"]:
        g.add_vertex(char)
        
    # Connecting vertices (Edges)
    g.add_edge("A", "B")
    g.add_edge("B", "C")
    g.add_edge("C", "D")
    g.add_edge("D", "A") # Creating a cycle A-B-C-D-A
    
    g.display()

if __name__ == "__main__":
    main()

"""
Input/Output Examples:
Output:
In-Order Traversal (Sorted result): [5, 10, 15, 20, 30]
...
Vertex A: ['B', 'D']
Vertex B: ['A', 'C']
Vertex C: ['B', 'D']
Vertex D: ['C', 'A']
...
"""
