# Island Perimeter

This project contains a Python function that calculates the perimeter of an island in a grid. The grid is represented by a 2D list of integers, where 0 represents water and 1 represents land.

## Problem Description

Given a grid where:

- 0 represents water
- 1 represents land
- Each cell is square, with a side length of 1
- Cells are connected horizontally/vertically (not diagonally)
- The grid is rectangular, with its width and height not exceeding 100
- The grid is completely surrounded by water
- There is only one island (or nothing)
- The island doesn't have "lakes" (water inside that isn't connected to the water surrounding the island)

The task is to calculate and return the perimeter of the island.

## Implementation

We have implemented two solutions for this problem:

1. **Iterative Approach**: This method iterates through each cell in the grid, counting the contribution of each land cell to the perimeter.

2. **Depth-First Search (DFS) Approach**: This method uses recursive DFS to explore the island and calculate its perimeter.

## Function Signature

```python
def island_perimeter(grid: List[List[int]]) -> int:
    """
    Calculate the perimeter of the island in the given grid.
    """
```

## DFS Implementation

The DFS implementation uses a recursive approach to explore the island:

- It starts from the first land cell it finds.
- It recursively explores adjacent cells, marking visited cells to avoid double-counting.
- Water cells and out-of-bounds cells contribute 1 to the perimeter.
- The function returns the total perimeter once all connected land cells have been explored.

## Example

```python
grid = [
    [0, 0, 0, 0, 0, 0],
    [0, 1, 0, 0, 0, 0],
    [0, 1, 0, 0, 0, 0],
    [0, 1, 1, 1, 0, 0],
    [0, 0, 0, 0, 0, 0]
]
print(island_perimeter(grid))  # Output: 12
```

## Files

- `0-island_perimeter.py`: Contains the implementation of the `island_perimeter` function.
- `0-main.py`: A main file to test the `island_perimeter` function.

## Usage

To run the example:

```bash
./0-main.py
```

This will execute the main file and print the perimeter of the island defined in the grid.

## Author

Edwin Orioki Kenyansa
