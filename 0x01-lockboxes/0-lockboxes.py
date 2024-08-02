#!/usr/bin/python3
"""
The lock boxes puzzle
"""


def canUnlockAll(boxes):
    """
    Checking if all boxes can be opened
    """
    n = len(boxes)
    opened = set()
    queue = set([0])

    while queue:
        box = queue.pop()
        if box not in opened:
            opened.add(box)
            for key in boxes[box]:
                if key < n and key not in opened:
                    queue.add(key)

    return len(opened) == n
