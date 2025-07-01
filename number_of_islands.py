"""
The Problem: Number of Islands
You're given an m x n 2D binary grid, grid, where 1 represents land and 0 represents water. 
Your task is to count the number of islands.

An island is formed by connecting adjacent lands horizontally or vertically. 
You can assume all four edges of the grid are surrounded by water.

Example:

Input: grid = [
    [1, 1, 0, 0, 0],
    [1, 1, 0, 0, 0],
    [0, 0, 1, 0, 0],
    [0, 0, 0, 1, 1]
]

Output: 3

Explanation: There are three distinct islands in this grid.
"""

def count_islands(grid):
    
    def submerge_island(grid, r, c):
        if grid[r][c] == 1:
            grid[r][c] = 0
            for i, j in [(-1, 0), (0, 1), (1, 0), (0, -1)]:
                if 0 <= r + i < len(grid) and 0 <= c + j < len(grid[0]):
                    submerge_island(grid, r + i, c + j)
    
    island_count = 0
    
    if grid:
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 1:
                    island_count += 1
                    submerge_island(grid, r, c)
    
    return island_count

if __name__ == "__main__":
    g = []
    assert count_islands(g) == 0

    g = [[0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0]]
    assert count_islands(g) == 0

    g = [[1, 1, 0, 1, 1],
         [1, 0, 1, 0, 1],
         [0, 0, 1, 0, 1],
         [0, 0, 0, 1, 1]]
    assert count_islands(g) == 3
    
    g = [[1, 1, 0, 0, 0],
         [1, 1, 0, 0, 0],
         [0, 0, 1, 0, 0],
         [0, 0, 0, 1, 1]]
    assert count_islands(g) == 3

    g = [[1, 1, 0, 0, 1],
         [1, 1, 0, 1, 0],
         [1, 0, 0, 1, 0],
         [1, 1, 1, 1, 1]]
    assert count_islands(g) == 2

    g = [[1, 1, 0, 1, 1],
         [1, 1, 0, 0, 1],
         [1, 1, 1, 0, 1],
         [0, 0, 1, 1, 1]]
    assert count_islands(g) == 1

    g = [[1, 0, 0, 1, 1],
         [0, 1, 0, 1, 1],
         [0, 0, 1, 0, 1],
         [0, 0, 0, 1, 0]]
    assert count_islands(g) == 5

    g = [[0, 0, 0, 0, 0],
         [0, 1, 1, 1, 0],
         [0, 1, 0, 1, 0],
         [0, 1, 1, 1, 0]]
    assert count_islands(g) == 1