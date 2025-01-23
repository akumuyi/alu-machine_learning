
# Linear Algebra Project

## Description
This project is part of the **ALU Machine Learning** curriculum and focuses on fundamental concepts in linear algebra, including vectors, matrices, matrix operations, and their implementation using Python and NumPy. The project is designed to help me understand and apply linear algebra concepts in machine learning.

## Learning Objectives
By the end of this project, you should be able to explain the following concepts without the help of Google:
- What is a vector?
- What is a matrix?
- What is a transpose?
- What is the shape of a matrix?
- What is an axis?
- What is a slice?
- How do you slice a vector/matrix?
- What are element-wise operations?
- How do you concatenate vectors/matrices?
- What is the dot product?
- What is matrix multiplication?
- What is NumPy?
- What is parallelization and why is it important?
- What is broadcasting?

## Resources
- [Introduction to vectors](https://www.khanacademy.org/math/linear-algebra/vectors-and-spaces)
- [What is a matrix?](https://www.mathsisfun.com/algebra/matrix-introduction.html)
- [Transpose](https://en.wikipedia.org/wiki/Transpose)
- [Understanding the dot product](https://www.mathsisfun.com/algebra/vectors-dot-product.html)
- [Matrix Multiplication](https://www.mathsisfun.com/algebra/matrix-multiplying.html)
- [NumPy Tutorial](https://numpy.org/doc/stable/user/quickstart.html)
- [NumPy Basics](https://numpy.org/doc/stable/user/basics.html)
- [Broadcasting](https://numpy.org/doc/stable/user/basics.broadcasting.html)

## Requirements
### Python Scripts
- Allowed editors: `vi`, `vim`, `emacs`
- All files will be interpreted/compiled on Ubuntu 16.04 LTS using `python3` (version 3.5)
- All files should end with a new line
- The first line of all your files should be exactly `#!/usr/bin/env python3`
- A `README.md` file at the root of the project folder is mandatory
- Your code should follow the `pycodestyle` (version 2.5)
- All modules, classes, and functions should have documentation
- All files must be executable

## Tasks
### 0. Slice Me Up
- **File**: `0-slice_me_up.py`
- **Description**: Complete the source code to slice an array into specific parts without using loops or conditional statements.

### 1. Trim Me Down
- **File**: `1-trim_me_down.py`
- **Description**: Complete the source code to extract specific columns from a matrix using only one `for` loop.

### 2. Size Me Please
- **File**: `2-size_me_please.py`
- **Description**: Write a function `matrix_shape(matrix)` that calculates the shape of a matrix.

### 3. Flip Me Over
- **File**: `3-flip_me_over.py`
- **Description**: Write a function `matrix_transpose(matrix)` that returns the transpose of a 2D matrix.

### 4. Line Up
- **File**: `4-line_up.py`
- **Description**: Write a function `add_arrays(arr1, arr2)` that adds two arrays element-wise.

### 5. Across The Planes
- **File**: `5-across_the_planes.py`
- **Description**: Write a function `add_matrices2D(mat1, mat2)` that adds two 2D matrices element-wise.

### 6. Howdy Partner
- **File**: `6-howdy_partner.py`
- **Description**: Write a function `cat_arrays(arr1, arr2)` that concatenates two arrays.

### 7. Gettin’ Cozy
- **File**: `7-gettin_cozy.py`
- **Description**: Write a function `cat_matrices2D(mat1, mat2, axis=0)` that concatenates two matrices along a specific axis.

### 8. Ridin’ Bareback
- **File**: `8-ridin_bareback.py`
- **Description**: Write a function `mat_mul(mat1, mat2)` that performs matrix multiplication.

### 9. Let The Butcher Slice It
- **File**: `9-let_the_butcher_slice_it.py`
- **Description**: Complete the source code to slice a matrix into specific parts without using loops or conditional statements.

### 10. I’ll Use My Scale
- **File**: `10-ill_use_my_scale.py`
- **Description**: Write a function `np_shape(matrix)` that calculates the shape of a `numpy.ndarray`.

### 11. The Western Exchange
- **File**: `11-the_western_exchange.py`
- **Description**: Write a function `np_transpose(matrix)` that transposes a matrix.

### 12. Bracing The Elements
- **File**: `12-bracin_the_elements.py`
- **Description**: Write a function `np_elementwise(mat1, mat2)` that performs element-wise addition, subtraction, multiplication, and division.

### 13. Cat's Got Your Tongue
- **File**: `13-cats_got_your_tongue.py`
- **Description**: Write a function `np_cat(mat1, mat2, axis=0)` that concatenates two matrices along a specific axis.

### 14. Saddle Up
- **File**: `14-saddle_up.py`
- **Description**: Write a function `np_matmul(mat1, mat2)` that performs matrix multiplication.

## Installation
To set up the environment for this project, follow these steps:

1. **Install Ubuntu 16.04 and Python 3.5**:
   - Use Vagrant with `ubuntu/xenial64`.

2. **Install pip 19.1**:
   ```bash
   wget https://bootstrap.pypa.io/get-pip.py
   sudo python3 get-pip.py
   rm get-pip.py
   ```

3. **Install NumPy, SciPy, and pycodestyle**:
   ```bash
   pip install --user numpy==1.15
   pip install --user scipy==1.3
   pip install --user pycodestyle==2.5
   ```

## Usage
To run any of the scripts, use the following command:
```bash
./<script_name>.py
```

## Repository
- **GitHub Repository**: [alu-machine_learning](https://github.com/your-username/alu-machine_learning)
- **Directory**: `math/linear_algebra`
