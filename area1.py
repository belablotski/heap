# Find the largest area of 1 in a 2D array

def largest_area_of_1(matrix):
    def dfs(matrix, i, j):
        if i < 0 or i >= len(matrix) or j < 0 or j >= len(matrix[0]) or matrix[i][j] != 1:
            return 0
        matrix[i][j] = 0
        return 1 + dfs(matrix, i + 1, j) + dfs(matrix, i - 1, j) + dfs(matrix, i, j + 1) + dfs(matrix, i, j - 1)

    max_area = 0
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j] == 1:
                max_area = max(max_area, dfs(matrix, i, j))
    return max_area

matrix = [
    [1, 1, 1, 1, 0],
    [1, 1, 0, 1, 0],
    [0, 1, 1, 1, 1],
    [0, 1, 0, 1, 1],
    [1, 1, 1, 1, 0]
]

print(largest_area_of_1(matrix))  # 4
