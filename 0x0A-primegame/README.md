# Prime Game

## Description

This project implements a solution for the Prime Game, a mathematical game where two players take turns removing prime numbers and their multiples from a set of consecutive integers. The goal is to determine the winner of multiple rounds of this game.

## Project Details

- **Algorithm Category**: Game Theory, Number Theory
- **Language**: Python

## Problem Statement

Maria and Ben play x rounds of a game, where in each round:

1. They start with a set of consecutive integers from 1 to n.
2. Players take turns choosing a prime number from the set.
3. The chosen number and its multiples are removed from the set.
4. The player who cannot make a move loses the round.
5. Maria always goes first.

The task is to determine who wins the most rounds, given the number of rounds (x) and an array of n values for each round.

## File Structure

- `0-prime_game.py`: Contains the main implementation of the isWinner function.
- `main_0.py`: A sample main file to test the implementation.

## Function Prototype

```python
def isWinner(x, nums)
```

- `x`: The number of rounds
- `nums`: An array of n values for each round
- Returns: Name of the player that won the most rounds, or None if it's a tie

## Usage

To run the program:

1. Ensure you have the required Python version installed.
2. Place the `0-prime_game.py` file in your working directory.
3. Create a main file (e.g., `main_0.py`) with the following content:

```python
#!/usr/bin/python3

isWinner = __import__('0-prime_game').isWinner

print("Winner: {}".format(isWinner(5, [2, 5, 1, 4, 3])))
```

4. Make the main file executable:

```
chmod +x main_0.py
```

5. Run the main file:

```
./main_0.py
```

## Example Output

```
Winner: Ben
```

## Note

- The implementation assumes both players play optimally.
- The solution uses dynamic programming principles for efficiency.
- The maximum value for n and x is 10000.

## Author

Edwin Orioki Kenyansa
