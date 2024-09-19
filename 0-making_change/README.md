# 0x08. Making Change

## Overview

This project tackles the classic "Making Change" problem, which is a common algorithm challenge in computer science. The goal is to determine the minimum number of coins needed to make up a given amount, given a list of coin denominations.

## Concepts Needed

### 1. Greedy Algorithms

- A greedy algorithm makes the locally optimal choice at each step.
- In the context of the coin change problem, it would always choose the largest coin possible at each step.
- While often fast, greedy algorithms don't always yield the optimal solution for all coin systems.

### 2. Dynamic Programming

- Dynamic Programming (DP) is used to solve optimization problems by breaking them down into simpler subproblems.
- It's particularly useful when subproblems overlap and have optimal substructure.
- In the coin change problem, DP can be used to build up solutions for larger amounts from solutions to smaller amounts.

### 3. Time and Space Complexity

- Understanding Big O notation is crucial for analyzing algorithm efficiency.
- The goal is to minimize both time and space complexity.
- For this problem, an efficient solution should have a time complexity better than O(n^2).

## Problem Statement

Given a pile of coins of different values, determine the fewest number of coins needed to meet a given amount total.

- Function Prototype: `def makeChange(coins, total)`
- Return: Fewest number of coins needed to meet total
- If total is 0 or less, return 0
- If total cannot be met by any number of coins you have, return -1
- `coins` is a list of the values of the coins in your possession
- The value of a coin will always be an integer greater than 0
- You can assume you have an infinite number of each denomination of coin in the list

## Code Implementation

The Python code implementing this solution is provided in the file `0-making_change.py`.

## Usage

```python
makeChange = __import__('0-making_change').makeChange

print(makeChange([1, 2, 25], 37))  # Output: 7
print(makeChange([1256, 54, 48, 16, 102], 1453))  # Output: -1
```

This solution efficiently solves the coin change problem, meeting the runtime evaluation criteria specified in the task.
