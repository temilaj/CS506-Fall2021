def calc_determinant(matrix, length):
    if length == 1:
        return matrix[0][0]
    if length == 2:
        return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]

    result = 0
    for i in range(length):
        if (i%2 == 0):
            result += matrix[0][i] * calc_determinant([row[:i] + row[i + 1:] for row in matrix[1:]], length - 1)
        else:
            result -= matrix[0][i] * calc_determinant([row[:i] + row[i + 1:] for row in matrix[1:]], length - 1)
    return result

def get_determinant(matrix):
    dimensionX, dimensionY = len(matrix[0]), len(matrix)

    is_square_matrix = dimensionX == dimensionY

    if is_square_matrix:
        length = len(matrix)
        return calc_determinant(matrix, length)
    else:
        raise ValueError