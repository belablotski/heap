"""
You are given a 2D grid representing a terrain. Each cell in the grid has an associated cost to traverse. 
You start at the top-left cell (0, 0) and want to reach the bottom-right cell (rows - 1, cols - 1). 
You can only move in four directions: up, down, left, or right.

Find the minimum total cost to travel from the start to the end cell.

Example:
grid = [
  [1, 3, 1],
  [1, 5, 1],
  [4, 2, 1]
]
The minimum cost path is (0, 0) -> (0, 1) -> (0, 2) -> (1, 2) -> (2, 2), with a total cost of 7.
"""

def shortest_path(W):
    PL = [[None for j in range(len(W[i]))] for i in range(len(W))]

    def bfs(r, c, path_len):
        pos = [(r, c, W[r][c])]

        while pos:
            r, c, path_len = pos.pop(0)

            if PL[r][c] is None or PL[r][c] >= path_len:
                PL[r][c] = path_len
                if 0 <= r-1 < len(W):
                    pos.append((r-1, c, path_len+W[r-1][c]))
                if 0 <= r+1 < len(W):
                    pos.append((r+1, c, path_len+W[r+1][c]))
                if 0 <= c-1 < len(W[r]):
                    pos.append((r, c-1, path_len+W[r][c-1]))
                if 0 <= c+1 < len(W[r]):
                    pos.append((r, c+1, path_len+W[r][c+1]))

    def dfs(r, c, exit_r, exit_c):
        if r == exit_r and c == exit_c:
            return [[(r, c, PL[r][c])]]
        else:
            pos = []
            if 0 <= r-1 < len(PL):
                pos.append((r-1, c, PL[r-1][c]))
            if 0 <= r+1 < len(PL):
                pos.append((r+1, c, PL[r+1][c]))
            if 0 <= c-1 < len(PL[r]):
                pos.append((r, c-1, PL[r][c-1]))
            if 0 <= c+1 < len(PL[r]):
                pos.append((r, c+1, PL[r][c+1]))
            paths = []
            for ps in [p for p in pos if p[2] == min([x[2] for x in pos])]:
                paths += [[(r, c, PL[r][c])] + x for x in dfs(ps[0], ps[1], exit_r, exit_c)]
            return paths

    # Build matrix of paths lenght
    exit_r, exit_c = len(W)-1, len(W[-1])-1
    bfs(exit_r, exit_c, 0)
    print('\n'.join(['\t'.join([str(c) for c in r]) for r in PL]))

    # Find min path
    enter_r = enter_c = 0
    paths = dfs(enter_r, enter_c, exit_r, exit_c)
    print(paths)
    for path in paths:
        print(f'Lenght {path[0][2]}: ' + ' -> '.join([f'({p[0]}, {p[1]})' for p in path]))
    return paths

def test_shortest_path():
    grid = [[0]]
    assert shortest_path(grid) == [[(0, 0, 0)]]
    
    grid = [[1, 3, 1],
            [1, 5, 1],
            [4, 2, 1]]
    assert shortest_path(grid) == [[(0, 0, 7), (0, 1, 6), (0, 2, 3), (1, 2, 2), (2, 2, 1)]]

    grid = [[1, 1, 1],
            [1, 2, 1],
            [1, 1, 1]]
    assert shortest_path(grid) == [[(0, 0, 5), (1, 0, 4), (2, 0, 3), (2, 1, 2), (2, 2, 1)], [(0, 0, 5), (0, 1, 4), (0, 2, 3), (1, 2, 2), (2, 2, 1)]]

    grid = [[1, 1, 1, 1, 1, 1],
            [1, 9, 1, 9, 1, 1],
            [1, 9, 1, 9, 1, 1],
            [1, 9, 1, 9, 1, 5],
            [1, 9, 9, 9, 1, 1],
            [1, 1, 1, 1, 1, 1]]
    assert shortest_path(grid) == [[(0, 0, 11), (1, 0, 10), (2, 0, 9), (3, 0, 8), (4, 0, 7), (5, 0, 6), (5, 1, 5), (5, 2, 4), (5, 3, 3), (5, 4, 2), (5, 5, 1)], [(0, 0, 11), (0, 1, 10), (0, 2, 9), (0, 3, 8), (0, 4, 7), (1, 4, 6), (2, 4, 5), (3, 4, 4), (4, 4, 3), (5, 4, 2), (5, 5, 1)], [(0, 0, 11), (0, 1, 10), (0, 2, 9), (0, 3, 8), (0, 4, 7), (1, 4, 6), (2, 4, 5), (3, 4, 4), (4, 4, 3), (4, 5, 2), (5, 5, 1)]]

    grid = [[1, 1, 1, 1, 1, 1],
            [1, 9, 1, 9, 1, 1],
            [1, 9, 1, 9, 1, 1],
            [1, 9, 1, 1, 1, 5],
            [1, 9, 1, 9, 1, 1],
            [1, 1, 1, 1, 1, 1]]
    assert shortest_path(grid) == [[(0, 0, 11), (1, 0, 10), (2, 0, 9), (3, 0, 8), (4, 0, 7), (5, 0, 6), (5, 1, 5), (5, 2, 4), (5, 3, 3), (5, 4, 2), (5, 5, 1)], [(0, 0, 11), (0, 1, 10), (0, 2, 9), (1, 2, 8), (2, 2, 7), (3, 2, 6), (4, 2, 5), (5, 2, 4), (5, 3, 3), (5, 4, 2), (5, 5, 1)], [(0, 0, 11), (0, 1, 10), (0, 2, 9), (1, 2, 8), (2, 2, 7), (3, 2, 6), (3, 3, 5), (3, 4, 4), (4, 4, 3), (5, 4, 2), (5, 5, 1)], [(0, 0, 11), (0, 1, 10), (0, 2, 9), (1, 2, 8), (2, 2, 7), (3, 2, 6), (3, 3, 5), (3, 4, 4), (4, 4, 3), (4, 5, 2), (5, 5, 1)], [(0, 0, 11), (0, 1, 10), (0, 2, 9), (0, 3, 8), (0, 4, 7), (1, 4, 6), (2, 4, 5), (3, 4, 4), (4, 4, 3), (5, 4, 2), (5, 5, 1)], [(0, 0, 11), (0, 1, 10), (0, 2, 9), (0, 3, 8), (0, 4, 7), (1, 4, 6), (2, 4, 5), (3, 4, 4), (4, 4, 3), (4, 5, 2), (5, 5, 1)]]

    grid = [[1, 1, 1, 2, 1, 1],
            [1, 9, 1, 9, 1, 1],
            [1, 9, 1, 9, 1, 1],
            [1, 9, 1, 1, 1, 5],
            [1, 9, 1, 9, 1, 1],
            [1, 2, 1, 1, 1, 1]]
    assert shortest_path(grid) == [[(0, 0, 11), (0, 1, 10), (0, 2, 9), (1, 2, 8), (2, 2, 7), (3, 2, 6), (4, 2, 5), (5, 2, 4), (5, 3, 3), (5, 4, 2), (5, 5, 1)], [(0, 0, 11), (0, 1, 10), (0, 2, 9), (1, 2, 8), (2, 2, 7), (3, 2, 6), (3, 3, 5), (3, 4, 4), (4, 4, 3), (5, 4, 2), (5, 5, 1)], [(0, 0, 11), (0, 1, 10), (0, 2, 9), (1, 2, 8), (2, 2, 7), (3, 2, 6), (3, 3, 5), (3, 4, 4), (4, 4, 3), (4, 5, 2), (5, 5, 1)]]

test_shortest_path()
