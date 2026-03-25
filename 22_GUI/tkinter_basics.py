"""
📁 22_GUI/tkinter_basics.py
🧠 Topic: Python GUI Programming (Tkinter Basics)

Key Concepts Covered:
1. Root Window (Tk)
2. Widgets (Label, Button, Entry)
3. Grid and Pack Layouts
4. Event Handling (Button clicks)
5. Geometry management (geometry, title)
6. Mainloop (The event loop)

Interview Focus:
- Why use Tkinter? (Built-in, lightweight, platform-independent)
- Difference between pack() and grid()? (Linear vs Cell-based layout)
- Role of mainloop()? (Keep app running and listening for events)
- How to pass data from an entry box to a function? (Using .get())
"""

import tkinter as tk
from tkinter import messagebox

# 1. ROOT WINDOW Setup
class MyGUIApp:
    """ Class-based GUI management. """
    def __init__(self, root):
        self.root = root
        self.root.title("Python Tkinter Practice")
        self.root.geometry("400x300")
        
        # 2. DESIGN: Widgets (Label, Entry, Button)
        
        # Label
        self.label = tk.Label(root, text="Enter your name:", font=("Arial", 12))
        self.label.pack(pady=10) # Using PACK for simple vertical stacking
        
        # Entry (Input box)
        self.name_entry = tk.Entry(root, font=("Arial", 11))
        self.name_entry.pack(pady=5)
        
        # Button
        self.greet_btn = tk.Button(root, text="Click Here!", command=self.on_button_click, bg="blue", fg="white")
        self.greet_btn.pack(pady=20)
        
        # Another label for dynamic result
        self.result_label = tk.Label(root, text="", font=("Arial", 10), fg="green")
        self.result_label.pack(pady=10)

    # 3. LOGIC: Event Handler
    def on_button_click(self):
        """ Code that runs when the button is clicked. """
        name = self.name_entry.get()
        
        if name:
            msg = f"Hello, {name}! Welcome to Python GUI."
            self.result_label.config(text=msg)
            # messagebox showing a popup
            messagebox.showinfo("Greeting Success", msg)
        else:
            messagebox.showwarning("Input Error", "Please enter a name first.")

def main():
    """ 
    Execution logic for GUI. 
    Note: On cloud/headless systems, this will error with '_tkinter.TclError'.
    Run this locally on your machine.
    """
    print("🚀 Starting Python Tkinter GUI App...")
    
    try:
        root = tk.Tk()
        app = MyGUIApp(root)
        
        # 4. FINISH: Event Loop (Keep window alive)
        print("Main GUI Loop running. Close the window to terminate.")
        # root.mainloop() # COMMENTED OUT to avoid hanging non-interactive environments
    except Exception as e:
        print(f"GUI ERROR: {e} (Likely running in a shell without display support)")

if __name__ == "__main__":
    main()

"""
Input/Output Examples:
Output:
Starting Python Tkinter GUI App...
GUI Main Loop running...
...
Event: User enters 'Alice' and clicks button.
Result: Label updates to 'Hello, Alice!' and a popup appears.
"""
