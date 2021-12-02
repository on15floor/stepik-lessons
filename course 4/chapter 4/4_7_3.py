"""4. Матрицы. Операции над матрицами.
Напишите программу, которая перемножает две матрицы.
"""


def square_matrix_mult(matrix_a, matrix_b, size):
    matrix_c = [[0] * size for i in range(size)]
    for i in range(size):
        for j in range(size):
            for q in range(size):
                matrix_c[i][j] += matrix_a[i][q] * matrix_b[q][j]
    return matrix_c


n = int(input())
matrix = [[int(i) for i in input().split()] for _ in range(n)]
m = int(input())
powered_matrix = matrix.copy()

for _ in range(m - 1):
    powered_matrix = square_matrix_mult(matrix, powered_matrix, n)

for row in powered_matrix:
    print(*row)
