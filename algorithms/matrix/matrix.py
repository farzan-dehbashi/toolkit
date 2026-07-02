def rotate_90(matrix):
    """Rotate NxN matrix 90 degrees clockwise in-place."""
    n = len(matrix)
    # Transpose
    for i in range(n):
        for j in range(i + 1, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
    # Reverse each row
    for row in matrix:
        row.reverse()
    return matrix


def spiral_order(matrix):
    """Return elements in spiral order."""
    result = []
    while matrix:
        result += matrix.pop(0)
        matrix = list(zip(*matrix))[::-1]
    return result


def zero_matrix(matrix):
    """Set entire row and column to 0 if an element is 0."""
    rows = set()
    cols = set()
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j] == 0:
                rows.add(i)
                cols.add(j)
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if i in rows or j in cols:
                matrix[i][j] = 0
    return matrix


if __name__ == "__main__":
    m = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    print(rotate_90(m))
    print(spiral_order([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))
