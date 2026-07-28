# =============================================================================
# PROGRAMMING FUNDAMENTALS — Assignment 4
# Topic: Multi-dimensional Arrays (2D Lists), Nested Loops, and Functions
# =============================================================================
#
# TASK: Matrix Operations
#
# Write a Python program that performs three operations on matrices (2D lists),
# each implemented in its own function.
#
# -----------------------------------------------------------------------------
# PART A — Transpose a Matrix
# -----------------------------------------------------------------------------
# - Read an M x N matrix from the user.
# - Compute and display its transpose (rows become columns, columns become rows).
#
# Example (2 x 3 input):
#
#   Original Matrix:      Transposed Matrix:
#   1  2  3               1  4
#   4  5  6               2  5
#                         3  6
#
# -----------------------------------------------------------------------------
# PART B — Add Two Matrices
# -----------------------------------------------------------------------------
# - Read two matrices of exactly the same size (M x N).
# - Compute their element-wise sum and display the result.
#   (Each position in the result = the sum of the values at that position
#    in both matrices.)
#
# -----------------------------------------------------------------------------
# PART C — Multiply Two Matrices
# -----------------------------------------------------------------------------
# - Read matrix A of size M x N and matrix B of size N x P.
#   (The number of COLUMNS in A must equal the number of ROWS in B.)
# - Compute and display the matrix product A × B (result is M x P).
#
# -----------------------------------------------------------------------------
# EXPECTED INPUT FORMAT
# -----------------------------------------------------------------------------
# When entering a row, the user types all values on one line separated by spaces:
#
#   Enter number of rows: 2
#   Enter number of columns: 3
#   Enter row 1: 1 2 3
#   Enter row 2: 4 5 6
#
# -----------------------------------------------------------------------------
# REQUIREMENTS
# -----------------------------------------------------------------------------
# - Use nested loops for all operations (no NumPy or other libraries).
# - Each operation must be in its own function (see scaffold below).
# - Display each matrix in a neat, aligned grid format.
# - Tip: Complete Part A first, then Parts B and C.
#

#
# =============================================================================
# YOUR CODE BELOW — remove the # symbols from the scaffold and fill it in
# =============================================================================
def read_matrix(rows, cols):
    matrix = []

    for i in range(rows):
        row = list(map(int, input("Enter row " + str(i + 1) + ": ").split()))

        while len(row) != cols:
            print("Please enter exactly", cols, "numbers.")
            row = list(map(int, input("Enter row " + str(i + 1) + ": ").split()))

        matrix.append(row)

    return matrix


def print_matrix(matrix):
    for row in matrix:
        for value in row:
            print(value, end=" ")
        print()


def transpose(matrix):
    result = []

    rows = len(matrix)
    cols = len(matrix[0])

    for i in range(cols):
        new_row = []
        for j in range(rows):
            new_row.append(matrix[j][i])
        result.append(new_row)

    return result


def add_matrices(matrix1, matrix2):
    result = []

    for i in range(len(matrix1)):
        row = []
        for j in range(len(matrix1[0])):
            row.append(matrix1[i][j] + matrix2[i][j])
        result.append(row)

    return result


def multiply_matrices(matrix1, matrix2):
    result = []

    for i in range(len(matrix1)):
        row = []
        for j in range(len(matrix2[0])):
            total = 0
            for k in range(len(matrix2)):
                total += matrix1[i][k] * matrix2[k][j]
            row.append(total)
        result.append(row)

    return result


def main():

    print("PART A - Transpose Matrix")

    rows = int(input("Enter number of rows:2 "))
    cols = int(input("Enter number of columns:3 "))

    print("Enter the matrix ")
    matrix = read_matrix(rows, cols)

    print("\nOriginal Matrix")
    print_matrix(matrix)

    print("\nTransposed Matrix")
    print_matrix(transpose(matrix))

    print("\nPART B - Add Two Matrices")

    rows = int(input("Enter number of rows: "))
    cols = int(input("Enter number of columns: "))

    print("Enter Matrix 1")
    matrix1 = read_matrix(rows, cols)

    print("Enter Matrix 2")
    matrix2 = read_matrix(rows, cols)

    print("\nSum of Matrices")
    print_matrix(add_matrices(matrix1, matrix2))

    print("\nPART C - Multiply Two Matrices")

    rows1 = int(input("Rows of Matrix A: "))
    cols1 = int(input("Columns of Matrix A: "))

    print("Enter Matrix A")
    matrixA = read_matrix(rows1, cols1)

    rows2 = int(input("Rows of Matrix B: "))
    cols2 = int(input("Columns of Matrix B: "))

    if cols1 != rows2:
        print("Matrices cannot be multiplied.")
    else:
        print("Enter Matrix B")
        matrixB = read_matrix(rows2, cols2)

        print("\nProduct Matrix")
        print_matrix(multiply_matrices(matrixA, matrixB))
