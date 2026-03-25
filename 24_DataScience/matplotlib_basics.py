"""
📁 24_DataScience/matplotlib_basics.py
🧠 Topic: Python for Data Science (Matplotlib Visualization)

Key Concepts Covered:
1. Plotting (plt.plot)
2. Bar Charts (plt.bar)
3. Scatter Plots (plt.scatter)
4. Plot Customization (Labels, Title, Legend)
5. Multiple subplots (plt.subplot)
6. Saving plots to disk (plt.savefig)

Interview Focus:
- Why use data visualization? (Patterns, trends, outliers detection)
- Difference between show() and savefig()? (Display vs Persist)
- What is a subplot? (Multiple charts in one figure)
- When to use a Bar Chart vs Scatter Plot? (Category comparison vs Correlation)
"""

import matplotlib.pyplot as plt
import numpy as np

def demonstrate_line_plot():
    """ 
    Showing trends over time/sequence. 
    Ideal for growth charts.
    """
    print("\n--- Generating Line Plot ---")
    
    # 1. Data Points
    x_years = [2021, 2022, 2023, 2024, 2025]
    y_revenue = [5000, 7500, 12000, 18000, 25000]
    
    # 2. Creating the plot
    plt.figure(figsize=(8, 5))
    plt.plot(x_years, y_revenue, marker='o', color='green', linestyle='--', label='Revenue ($)')
    
    # 3. Adding details
    plt.title("Company Growth (2021-2025)")
    plt.xlabel("Fiscal Year")
    plt.ylabel("Revenue (USD)")
    plt.legend()
    plt.grid(True)
    
    # 4. Saving plot as an image (since show() may block non-interactive headless sessions)
    plt.savefig("growth_chart.png")
    print("Optimization: Plot saved as 'growth_chart.png'.")

def demonstrate_bar_chart():
    """ 
    Comparing categories. 
    Ideal for product sales or department counts.
    """
    print("\n--- Generating Bar Chart ---")
    
    products = ["Laptop", "Mouse", "Keyboard", "Monitor"]
    sales_units = [45, 90, 75, 40]
    
    plt.figure(figsize=(8, 5))
    plt.bar(products, sales_units, color=['blue', 'orange', 'green', 'red'])
    
    plt.title("Product Sales Distribution")
    plt.xlabel("Electronics Category")
    plt.ylabel("Units Sold")
    
    plt.savefig("sales_bar_chart.png")
    print("Optimization: Plot saved as 'sales_bar_chart.png'.")

def demonstrate_scatter_plot():
    """ 
    Showing correlations between two variables. 
    Ideal for experimental data.
    """
    print("\n--- Generating Scatter Plot ---")
    
    # Random data generation with NumPy
    np.random.seed(42)
    study_hours = np.random.uniform(1, 10, 50)
    exam_score = 40 + (5 * study_hours) + np.random.normal(0, 5, 50)
    
    plt.figure(figsize=(8, 5))
    plt.scatter(study_hours, exam_score, alpha=0.6, color='purple')
    
    plt.title("Correlation: Study Hours vs Exam Score")
    plt.xlabel("Hours Studied")
    plt.ylabel("Final Score (%)")
    
    plt.savefig("score_scatter.png")
    print("Optimization: Plot saved as 'score_scatter.png'.")

def main():
    print("🚀 Python Data Visualization (Matplotlib) Practice")
    
    # Note: Requires 'matplotlib' to be installed (pip install matplotlib)
    try:
        demonstrate_line_plot()
        demonstrate_bar_chart()
        demonstrate_scatter_plot()
        print("\nAll plots generated successfully. Check the directory for local .png files.")
    except ImportError as e:
        print(f"LIBRARIES MISSING: {e}")
        print("Run 'pip install matplotlib' to test this file.")
    except Exception as e:
        print(f"ERROR: {e}")

if __name__ == "__main__":
    main()

"""
Input/Output Examples:
Output:
Generating Line Plot
Optimization: Plot saved as 'growth_chart.png'.
...
Generating Bar Chart
Optimization: Plot saved as 'sales_bar_chart.png'.
...
All plots generated successfully.
"""
