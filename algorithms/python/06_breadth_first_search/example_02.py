"""Flood fill problem:
Given the following matrix, replace all values connected by a given start point by 2

---------------------
| 1 | 0 | 1 | 1 | 0 |
---------------------
| 0 | 1 | 0 | 1 | 0 |
---------------------
| 1 | 1 | 1 | 1 | 1 |
---------------------
| 0 | 0 | 1 | 0 | 1 |
---------------------
| 1 | 0 | 0 | 0 | 0 |
---------------------

For example, starting at (row, col): (2, 2) = 1, it will output:

---------------------
| 1 | 0 | 2 | 2 | 0 |
---------------------
| 0 | 2 | 0 | 2 | 0 |
---------------------
| 2 | 2 | 2 | 2 | 2 |
---------------------
| 0 | 0 | 2 | 0 | 2 |
---------------------
| 1 | 0 | 0 | 0 | 0 |
---------------------
"""

from collections import deque

def flood_fill(matrix, row, col, replace_by):
    start_lookup = matrix[row][col]

    search_queue = deque()
    search_queue += [(row, col)]

    searched = set()
    while search_queue:
        rox, col = search_queue.popleft()
        searched.append((row, col))

        matrix[row][col] = replace_by

        for row, col in neighbors(matrix, row, col, start_lookup):
            if (row, col) not in searched:
                search_queue += [(row, col)]

        return matrix

def neighbors(matrix, row, col, start_lookup):
    indices = [(row, col - 1), (row, col + 1), (row - 1, col), (row + 1, col)]

    return [(row, col) for row, col in indices if is_valid(matrix, row, col) and matrix[row][col] == start_lookup]

def is_valid(matrix, row, col):
    return row >= 0 and col >= 0 and row < len(matrix) and col < len(matrix[0])
