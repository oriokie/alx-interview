#!/usr/bin/python3
"""
Module for calculating the perimeter of an island described in a grid.
"""


def island_perimeter(grid):
    """
    Calculate the perimeter of the island described in the grid using DFS.

    Args: grid

    Returns:
    int: The perimeter of the island.
    """
    if not grid or not grid[0]:
        return 0

    def dfs(i, j):
        if i < 0 or i >= len(grid) or j < 0 or j >= len(
                grid[0]) or grid[i][j] == 0:
            return 1  # Water edge, contribute to perimeter
        if (i, j) in visited:
            return 0  # Already visited land, don't contribute to perimeter

        visited.add((i, j))

        perimeter = 0
        perimeter += dfs(i - 1, j)  # Up
        perimeter += dfs(i + 1, j)  # Down
        perimeter += dfs(i, j - 1)  # Left
        perimeter += dfs(i, j + 1)  # Right

        return perimeter

    visited = set()
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == 1:
                return dfs(i, j)  # Start DFS from the first land cell found

    return 0  # No land found
