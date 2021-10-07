import pytest

from cs506 import matrix

@pytest.mark.parametrize('input_matrix, determinant', [
    (
        [[3, 8], [4, 6]],
        -14,
    ),
    (
        [[1,2], [3, 4]],
        -2
    ),
])
def test_read(input_matrix, determinant):
    actual_data = matrix.get_determinant(input_matrix)
    expected_data = determinant

    assert actual_data == expected_data