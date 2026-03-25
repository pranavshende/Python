"""
📁 24_DataScience/numpy_pandas.py
🧠 Topic: Python for Data Science (NumPy and Pandas Basics)

Key Concepts Covered:
1. NumPy Arrays (Creation, Shape, Operations)
2. NumPy Vectorization (Faster math)
3. Pandas Series (1D data with index)
4. Pandas DataFrames (2D tabular data)
5. Loading datasets (pd.read_csv)
6. Data Filtering and Statistics

Interview Focus:
- Why use NumPy over standard Python lists? (Homogeneous memory, O(1) element access, Vectorized speed)
- Difference between series and dataframe? (1D vs 2D)
- How to filter a dataframe? (Using loc/iloc or boolean masks)
- How to check missing values? (df.isnull())
- Benefit of DataFrames? (Handles large, heterogeneous data with labels)
"""

import numpy as np
import pandas as pd

def demonstrate_numpy_core():
    """ 
    Speed and Matrix Operations with NumPy. 
    Memory efficient arrays for mathematical computation.
    """
    print("\n--- NumPy Basics (Arrays) ---")
    
    # 1. Array creation
    arr = np.array([1, 2, 3, 4, 5])
    print(f"NumPy Array: {arr} (Type: {type(arr).__name__})")
    
    # 2. Reshaping (5 elements to 1x5 matrix)
    print(f"Shape: {arr.shape} | Size: {arr.size}")
    
    # 3. Vectorization (Adding 10 to every element at once)
    arr_new = arr + 10
    print(f"Vectorized addition (+10): {arr_new}")
    
    # 4. Built-in Math
    print(f"Array Mean: {np.mean(arr)} | Max: {np.max(arr)}")
    
    # 5. Multi-dimensional array (2x3)
    matrix = np.array([[1, 2, 3], [4, 5, 6]])
    print(f"2x3 Matrix:\n{matrix}")

def demonstrate_pandas_core():
    """ 
    Tabular Data Management with Pandas. 
    Like Excel/SQL inside Python.
    """
    print("\n--- Pandas Basics (DataFrames) ---")
    
    # 1. Data Source (Dictionary)
    data = {
        "Name": ["Alice", "Bob", "Charlie", "David"],
        "Age": [25, 30, 35, 40],
        "Score": [88, 92, 78, 95]
    }
    
    # 2. DataFrame Creation
    df = pd.DataFrame(data)
    print("Initial DataFrame:")
    print(df)
    
    # 3. Accessing columns
    print(f"\nNames column only:\n{df['Name']}")
    
    # 4. Statistical Summary
    print("\n--- DataFrame Statistics (.describe) ---")
    print(df.describe())
    
    # 5. Filtering data (High scorers > 90)
    high_scorers = df[df["Score"] > 90]
    print("\n--- Filtered: Score > 90 ---")
    print(high_scorers)
    
    # 6. Adding a New Column
    df["Status"] = ["Pass", "Pass", "Pass", "Pass"]
    print("\nDataFrame with new 'Status' column:")
    print(df)

def main():
    print("🚀 Python Data Science (NumPy/Pandas) Practice")
    
    # Note: These libraries must be installed (pip install numpy pandas)
    try:
        demonstrate_numpy_core()
        demonstrate_pandas_core()
    except ImportError as e:
        print(f"LIBRARIES MISSING: {e}")
        print("Run 'pip install numpy pandas' to test this file.")

if __name__ == "__main__":
    main()

"""
Input/Output Examples:
Output:
NumPy Array: [1 2 3 4 5]
Vectorized addition (+10): [11 12 13 14 15]
...
Initial DataFrame:
       Name  Age  Score
0     Alice   25     88
1       Bob   30     92
...
Filtered: Score > 90
  Name  Age  Score
1  Bob   30     92
...
"""
