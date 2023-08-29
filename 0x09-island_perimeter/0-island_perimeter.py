#!/usr/bin/python3
"""Island Perimeter"""


def island_perimeter(grid):
    """
    Returns the perimeter of the island described in grid
    """
    perimeter = 0
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == 1:
                if j-1 < 0 or grid[i][j-1] == 0:
                    perimeter += 1
                if j+1 >= len(grid[0]) or grid[i][j+1] == 0:
                    perimeter += 1
                if i-1 < 0 or grid[i-1][j] == 0:
                    perimeter += 1
                if i+1 >= len(grid) or grid[i+1][j] == 0:
                    perimeter += 1
    return perimeter
