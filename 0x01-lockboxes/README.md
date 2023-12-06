# Lockboxes Problem

## Overview

This Python script provides a solution to the "lockboxes" problem. Given a set of sequentially numbered boxes, each containing keys to other boxes, the script determines if all the boxes can be opened.

## Function: canUnlockAll

### Description

```python
from collections import deque

def canUnlockAll(boxes):
    """
    Determine if all boxes can be opened.

    Args:
    - boxes (list of lists): Each box is represented as a list of positive integers.
      A key with the same number as a box opens that box.

    Returns:
    - bool: True if all boxes can be opened, False otherwise.
    """
    ### Implementation Details

    The `canUnlockAll` function utilizes a breadth-first search (BFS) algorithm to explore the boxes and check if all of them can be opened. Here's a high-level overview of the implementation:

    1. **Initialization:** The function initializes a boolean array `visited` to keep track of visited boxes. The first box (`boxes[0]`) is considered unlocked initially.

    2. **BFS:** The function uses a queue to perform BFS starting from the first box (`boxes[0]`). It explores all reachable boxes using the keys found in each box. If a key leads to an unvisited box, that box is marked as visited and added to the queue for further exploration.

    3. **Check:** After the BFS traversal, the function checks if all boxes have been visited. If so, it returns `True`, indicating that all boxes can be opened. Otherwise, it returns `False`.

    This approach ensures that the function explores all possible paths through the keys to determine if every box can be opened.

```
