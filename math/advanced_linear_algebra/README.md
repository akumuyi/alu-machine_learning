# Advanced Linear Algebra Project

## Project Overview
- **Start Date:** January 25, 2025, 12:00 AM
- **End Date:** January 31, 2025, 11:59 PM

## Learning Objectives
By the end of this project, you should be able to:
- **Explain** what a determinant is and how to calculate it.
- **Describe** minors, cofactors, and the adjugate of a matrix; including how to compute them.
- **Understand** the concept of matrix inverses and their calculation.
- **Discuss** eigenvalues and eigenvectors, along with their computation.
- **Determine** the definiteness of a matrix.

## Resources
- **Videos & Reading:**
  - [The determinant | Essence of linear algebra](https://www.youtube.com/watch?v=Ip3X9LOh2dk)
  - [Determinant of a Matrix](https://www.mathsisfun.com/algebra/matrix-determinant.html)
  - [Determinant](https://en.wikipedia.org/wiki/Determinant)
  - [Determinant of an empty matrix](https://math.stackexchange.com/questions/319992/determinant-of-an-empty-matrix)
  - [Inverse matrices, column space and null space](https://www.khanacademy.org/math/linear-algebra/matrix_transformations/inverse-transformations/v/inverse-matrices-column-space-and-null-space)
  - [Inverse of a Matrix using Minors, Cofactors and Adjugate](https://www.mathsisfun.com/algebra/matrix-inverse-minors-cofactors-adjugate.html)
  - [Minor](https://en.wikipedia.org/wiki/Minor_(linear_algebra))
  - [Cofactor](https://en.wikipedia.org/wiki/Cofactor_(linear_algebra))
  - [Adjugate matrix](https://en.wikipedia.org/wiki/Adjugate_matrix)
  - [Singular Matrix](https://en.wikipedia.org/wiki/Invertible_matrix#Singular_matrix)
  - [Elementary Matrix Operations](https://en.wikipedia.org/wiki/Elementary_matrix)
  - [Gaussian Elimination](https://en.wikipedia.org/wiki/Gaussian_elimination)
  - [Gauss-Jordan Elimination](https://en.wikipedia.org/wiki/Gaussian_elimination#Gauss–Jordan_elimination)
  - [Matrix Inverse](https://en.wikipedia.org/wiki/Invertible_matrix)
  - [Eigenvectors and eigenvalues | Essence of linear algebra](https://www.youtube.com/watch?v=PFDu9oVAE-g)
  - [Eigenvalues and eigenvectors](https://en.wikipedia.org/wiki/Eigenvalues_and_eigenvectors)
  - [Definiteness of a matrix Up to Eigenvalues](https://en.wikipedia.org/wiki/Definiteness_of_a_matrix)
  - [Tests for Positive Definiteness of a Matrix](https://www.math.uwaterloo.ca/~hwolkowi/henry/reports/talks.dir/posdef.pdf)
  - [Positive Definite Matrices and Minima](https://www.math.ubc.ca/~pwalls/math-python/linear-algebra/positive-definite/)

- **References:**
  - [numpy.linalg.eig](https://numpy.org/doc/stable/reference/generated/numpy.linalg.eig.html)

## Requirements
- **General:**
  - Allowed editors: `vi`, `vim`, `emacs`
  - All files will be interpreted/compiled on Ubuntu 16.04 LTS using Python 3 (version 3.5)
  - Your files will be executed with numpy (version 1.15)
  - Files should end with a new line
  - The first line of all your files should be exactly `#!/usr/bin/env python3`
  - A `README.md` file, at the root of the folder of the project, is mandatory
  - Your code should use the pycodestyle style (version 2.5)
  - All modules, classes, and functions should have documentation
  - No external modules allowed unless specified
  - All files must be executable
  - File length will be tested

## Project Tasks

### 0. Determinant
- **File:** `0-determinant.py`
- **Function:** `determinant(matrix)`

### 1. Minor
- **File:** `1-minor.py`
- **Function:** `minor(matrix)`

### 2. Cofactor
- **File:** `2-cofactor.py`
- **Function:** `cofactor(matrix)`

### 3. Adjugate
- **File:** `3-adjugate.py`
- **Function:** `adjugate(matrix)`

### 4. Inverse
- **File:** `4-inverse.py`
- **Function:** `inverse(matrix)`

### 5. Definiteness
- **File:** `5-definiteness.py`
- **Function:** `definiteness(matrix)`