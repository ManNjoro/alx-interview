#!/usr/bin/python3
"""
This script contains a function to
calculate the perimeter of an island in a grid.
"""


def island_perimeter(grid):
    """
    Calculates the perimeter of the island described in grid
    """
    def explore(grid, row, col, visited):
        rowInbounds = 0 <= row and row < len(grid)
        colInbounds = 0 <= col and col < len(grid[0])

        if not rowInbounds or not colInbounds:
            return 0

        if grid[row][col] == 0:
            return 0

        pos = (row, col)
        if (pos in visited):
            return 0
        visited.add(pos)
        size = 1
        size += explore(grid, row - 1, col, visited)
        size += explore(grid, row + 1, col, visited)
        explore(grid, row, col - 1, visited)
        explore(grid, row, col + 1, visited)
        return size

    visited = set()
    minSize = float('inf')
    for row in range(len(grid)):
        for col in range(len(grid[0])):
            size = explore(grid, row, col, visited)
            if size > 0 and size < minSize:
                minSize = size
    return minSize * 4
