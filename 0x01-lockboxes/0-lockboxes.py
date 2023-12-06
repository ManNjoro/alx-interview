#!/usr/bin/python3
"""
Determine if all boxes can be opened.
"""
from collections import deque


def canUnlockAll(boxes):
    """
    Determine if all boxes can be opened.

    Args:
    - boxes: Each box is represented as a list of positive integers.
      A key with the same number as a box opens that box.

    Returns:
    - bool: True if all boxes can be opened, False otherwise.
    """
    n = len(boxes)
    visited = [False] * n
    visited[0] = True  # The first box is unlocked initially
    queue = deque([0])  # Start with the first box

    while queue:
        current_box = queue.popleft()

        for key in boxes[current_box]:
            if not visited[key]:
                visited[key] = True
                queue.append(key)

    # Check if all boxes are visited
    return all(visited)
