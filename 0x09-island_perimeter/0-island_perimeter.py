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
    len_grid = len(grid)

    for row in range(len_grid):
        for col in range(row):
            if grid[row][col] == 1:
                if grid[row - 1][col] == 0 or grid[row + 1] == 0 \
                        or grid[row][col - 1] == 0 or grid[row][col + 1] == 0:
                    perimeter += 4
                else:
                    perimeter -= 2
    return perimeter


if __name__ == "__main__":
    grid = [
        [0, 0, 0, 0, 0, 0],
        [0, 1, 0, 0, 0, 0],
        [0, 1, 0, 0, 0, 0],
        [0, 1, 1, 1, 0, 0],
        [0, 0, 0, 0, 0, 0]
    ]
    print(island_perimeter(grid))
