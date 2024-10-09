#!/usr/bin/python3
"""This module contains island_perimeter function"""


def island_perimeter(grid):
    """
    Returns the perimeter of the island described in grid.

    Args:
        grid (list of list of int): A list of lists where:
        - 0 represents water
        - 1 represents land
        Each cell is square with a side length of 1.
        Cells are connected horizontally/vertically (not diagonally).
        The grid is completely surrounded by water.
        There is only one island (or nothing).
        The island doesn’t have “lakes”
        water inside that isn’t connected to the water surrounding the island

    Returns:
        int: The perimeter of the island.
    """

    parameter = 0
    ln_1 = len(grid)
    ln_2 = len(grid[0])
    for i in range(0, ln_1):
        for j in range(0, ln_2):
            if grid[i][j] == 1:
                if i == 0 or grid[i - 1][j] == 0:
                    parameter += 1
                if i == ln_1 - 1 or grid[i + 1][j] == 0:
                    parameter += 1
                if j == 0 or grid[i][j - 1] == 0:
                    parameter += 1
                if j == ln_2 - 1 or grid[i][j + 1] == 0:
                    parameter += 1
    return parameter
