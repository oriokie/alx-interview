# 0x07. Rotate 2D Matrix

## Overview

This project contains a Python implementation of an algorithm to rotate a 2D matrix 90 degrees clockwise. The rotation is performed in-place, which means the original matrix is modified without using additional data structures.

## Requirements

- Allowed editors: vi, vim, emacs
- All files interpreted/compiled on Ubuntu 20.04 LTS using python3 (version 3.8.10)
- All files should end with a new line
- The first line of all files should be exactly `#!/usr/bin/python3`
- A README.md file, at the root of the folder of the project, is mandatory
- Code should use the pycodestyle style (version 2.8.0)
- No external modules should be imported
- All modules and functions must be documented
- All files must be executable

## File Description

- `0-rotate_2d_matrix.py`: Contains the implementation of the `rotate_2d_matrix` function.

## Function Prototype

```python
def rotate_2d_matrix(matrix):
```

## Usage

```python
from 0-rotate_2d_matrix import rotate_2d_matrix

# Example usage
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

rotate_2d_matrix(matrix)
print(matrix)
```

## Example

Input:

```
[
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
```

Output (after rotation):

```
[
    [7, 4, 1],
    [8, 5, 2],
    [9, 6, 3]
]
```

## Author

Edwin Orioki Kenyansa
