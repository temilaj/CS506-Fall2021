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

# def get_determinant(matrix):
#     dimensionX, dimensionY = len(matrix[0]), len(matrix)

#     print(dimensionX, dimensionY)
#     is_square_matrix = dimensionX == dimensionY

#     if is_square_matrix:
#         length = len(matrix)
#         return calc_determinant(matrix, length)
#     else:
#         raise ValueError

def get_determinant(matrix):
    total = 0
    idx = list(range(len(matrix)))

    if len(matrix) == 0:
        return 0
    elif len(matrix) == 1 and len(matrix[0]) == 1:
        return matrix[0][0]
    elif len(matrix) == 2 and len(matrix[0]) == 2:
        total = matrix[0][0] * matrix[1][1] - matrix [0][1] * matrix[1][0]
        return total
    elif len(matrix) == len(matrix[0]):
        for i in idx:
            new_matrix = matrix.copy()
            new_matrix = new_matrix[1:] #create sub_matrix

            for j in range(len(new_matrix)):
                new_matrix[j] = new_matrix[j][0:i] + new_matrix[j][i+1:]

            sign = (-1) ** (i%2)
            sub_det = get_determinant(new_matrix)
            total += sign * matrix[0][i] * sub_det
    else:
        raise ValueError("It must be a nxn matrix!")

    return total


# matrix_a = np.array([[3, 8], [4, 6]])
matrix_a = [[3, 8], [4, 6]]
determinant_a = get_determinant(matrix_a)
print(determinant_a)

# matrix_b = np.array([[1,2], [3, 4]])
matrix_b = [[1,2], [3, 4]]
determinant_b = get_determinant(matrix_b)
print(determinant_b)

# matrix_c = np.array([[6,1,1], [4, -2, 5 ], [2, 8, 7]])
# determinant_c = get_determinant(matrix_c)
# print(determinant_c)