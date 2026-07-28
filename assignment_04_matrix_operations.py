def read_matrix(rows, cols, name="matrix"):
    print(f"Enter {name} ({rows}x{cols}):")
    matrix = []
    for i in range(rows):
        row = list(map(float, input(f"Enter row {i + 1}: ").split()))
        matrix.append(row)
    return matrix


def print_matrix(matrix):
    for row in matrix:
        print(" ".join(f"{val:6.1f}" for val in row))
    print()


def transpose_matrix(matrix):
    rows = len(matrix)
    cols = len(matrix[0])
    result = [[0] * rows for _ in range(cols)]

    for i in range(rows):
        for j in range(cols):
            result[j][i] = matrix[i][j]

    return result


def add_matrices(matrix_a, matrix_b):
    rows = len(matrix_a)
    cols = len(matrix_a[0])
    result = [[0] * cols for _ in range(rows)]

    for i in range(rows):
        for j in range(cols):
            result[i][j] = matrix_a[i][j] + matrix_b[i][j]

    return result


def multiply_matrices(matrix_a, matrix_b):
    rows_a = len(matrix_a)
    cols_a = len(matrix_a[0])
    cols_b = len(matrix_b[0])
    result = [[0] * cols_b for _ in range(rows_a)]

    for i in range(rows_a):
        for j in range(cols_b):
            total = 0
            for k in range(cols_a):
                total += matrix_a[i][k] * matrix_b[k][j]
            result[i][j] = total

    return result


if __name__ == "__main__":
    # ---------------- PART A: Transpose ----------------
    print("=== PART A: Transpose a Matrix ===")
    rows = int(input("Enter number of rows: "))
    cols = int(input("Enter number of columns: "))
    matrix = read_matrix(rows, cols)

    print("\nOriginal Matrix:")
    print_matrix(matrix)

    print("Transposed Matrix:")
    print_matrix(transpose_matrix(matrix))

    # ---------------- PART B: Addition ----------------
    print("=== PART B: Add Two Matrices ===")
    rows = int(input("Enter number of rows for both matrices: "))
    cols = int(input("Enter number of columns for both matrices: "))

    matrix_a = read_matrix(rows, cols, "Matrix A")
    matrix_b = read_matrix(rows, cols, "Matrix B")

    print("\nSum of Matrices:")
    print_matrix(add_matrices(matrix_a, matrix_b))

    # ---------------- PART C: Multiplication ----------------
    print("=== PART C: Multiply Two Matrices ===")
    rows_a = int(input("Enter number of rows for Matrix A: "))
    cols_a = int(input("Enter number of columns for Matrix A (= rows for Matrix B): "))
    cols_b = int(input("Enter number of columns for Matrix B: "))

    matrix_a = read_matrix(rows_a, cols_a, "Matrix A")
    matrix_b = read_matrix(cols_a, cols_b, "Matrix B")

    print("\nProduct of Matrices (A x B):")
    print_matrix(multiply_matrices(matrix_a, matrix_b))