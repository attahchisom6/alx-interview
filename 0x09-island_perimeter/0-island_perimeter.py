#!/usr/bin/python3
"""
solving for the perineter if an island
"""


def island_perimeter(grid):
    """
    function to get the perimeter of an island
    here webassune the island is surrounded byvwater (0) and each unit square
    in the island (1) has a perimeter of 4
    """
    perimeter = 0
    rows = len(grid)
    cols = len(grid[0])

    for row in range(rows):
        for col in range(cols):
            if grid[row][col] == 1:
                perimeter += 4
                # top check
                if row > 0 and grid[row - 1][col] == 1:
                    perimeter -= 1

                # bottom check Note row - 1 is the last row in 0-indexing sys
                if row < rows - 1 and grid[row + 1][col] == 1:
                    perimeter -= 1

                # left check
                if col > 0 and grid[row][col - 1] == 1:
                    perimeter -= 1

                # right check Note: col -1 is last column in 0-indexing system
                if col < cols - 1 and grid[row][col + 1] == 1:
                    perimeter -= 1

            elif grid[row][col] == 0:
                continue
    return perimeter
