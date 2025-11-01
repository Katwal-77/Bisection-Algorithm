# Numerical Analysis - Assignment 3: The Bisection Algorithm

## Overview
This project implements and visualizes the Bisection Method, a fundamental numerical technique for finding roots of continuous functions. The implementation is done in Python with Jupyter Notebook, and it includes a detailed HTML report with interactive visualizations.

## Features
- **Bisection Method Implementation**: A robust Python implementation of the bisection algorithm
- **Interactive Visualization**: Animated demonstration of the bisection method in action
- **Step-by-Step Explanation**: Detailed documentation of the algorithm and its mathematical foundation
- **Error Analysis**: Comprehensive analysis of the method's convergence and error bounds
- **Example Applications**: Practical examples demonstrating the method's usage

## Project Structure
```
Assignment_3/
├── Bisection_Algo.ipynb      # Jupyter Notebook with implementation
├── index.html               # Interactive HTML report
├── README.md                # This file
└── create_zip.py            # Utility script for creating submission package
```

## Prerequisites
- Python 3.6+
- Jupyter Notebook
- Required Python packages:
  - numpy
  - matplotlib
  - notebook

## Installation
1. Clone the repository or download the project files
2. Install the required packages:
   ```
   pip install numpy matplotlib notebook
   ```
3. Launch Jupyter Notebook:
   ```
   jupyter notebook
   ```
4. Open `Bisection_Algo.ipynb` to view and run the implementation
## Or If you don't want to dowanload jupyter notebook on your system 
1.you can copy the `Bisection_Algo.ipynb` ,then paste in colab.research


## Usage
1. Run the Jupyter Notebook to see the implementation and visualizations
2. The notebook includes example usage with the function f(x) = x³ - x - 2
3. View `index.html` in a web browser for the interactive report

## Example
```python
# Define the function to find roots for
def f(x):
    return x**3 - x - 2

# Find a root in the interval [1, 2]
root, iterations = bisection(f, 1, 2, tol=1e-6)
print(f"Approximate root: {root:.6f}")
print(f"Function value at root: {f(root):.10f}")
print(f"Number of iterations: {len(iterations)}")
```

## Visualization
The project includes an interactive visualization that shows:
- The function graph
- Interval updates during each iteration
- Convergence towards the root
- Error analysis

## Author
- **Prem Bahadur Katuwal** (202424080129)
- Computer Science and Engineering
- University of Electronic Science and Technology of China (UESTC)

## Submission
Submitted to: Prof. Xi-Le Zhao (2021-2024 World's Top 2% Scientists)

## License
This project is for educational purposes as part of the Numerical Analysis course at UESTC.
# Bisection-Algorithm
