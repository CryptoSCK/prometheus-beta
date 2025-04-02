"""
Test suite for matrix operations module.
"""

import pytest
from src.matrix_operations import add_matrices

def test_basic_matrix_addition():
    """Test standard matrix addition."""
    matrix1 = [[1, 2], [3, 4]]
    matrix2 = [[5, 6], [7, 8]]
    expected = [[6, 8], [10, 12]]
    assert add_matrices(matrix1, matrix2) == expected

def test_matrix_addition_with_float():
    """Test matrix addition with floating point numbers."""
    matrix1 = [[1.5, 2.5], [3.5, 4.5]]
    matrix2 = [[0.5, 1.5], [2.5, 3.5]]
    expected = [[2.0, 4.0], [6.0, 8.0]]
    assert add_matrices(matrix1, matrix2) == expected

def test_different_row_lengths_raises_error():
    """Test that matrices with inconsistent row lengths raise an error."""
    matrix1 = [[1, 2], [3, 4]]
    matrix2 = [[1, 2, 3], [4, 5, 6]]
    with pytest.raises(ValueError, match="Matrices must have the same number of columns"):
        add_matrices(matrix1, matrix2)

def test_different_matrix_sizes_raises_error():
    """Test that matrices with different row counts raise an error."""
    matrix1 = [[1, 2], [3, 4]]
    matrix2 = [[1, 2], [3, 4], [5, 6]]
    with pytest.raises(ValueError, match="Matrices must have the same number of rows"):
        add_matrices(matrix1, matrix2)

def test_non_numeric_elements_raises_error():
    """Test that non-numeric elements raise a TypeError."""
    matrix1 = [[1, 2], [3, 4]]
    matrix2 = [[1, 'a'], [3, 4]]
    with pytest.raises(TypeError, match="Matrix elements must be numeric"):
        add_matrices(matrix1, matrix2)

def test_empty_matrix_raises_error():
    """Test that empty matrices raise a ValueError."""
    matrix1 = []
    matrix2 = [[1, 2], [3, 4]]
    with pytest.raises(ValueError, match="Matrices cannot be empty"):
        add_matrices(matrix1, matrix2)

def test_non_list_input_raises_error():
    """Test that non-list inputs raise a TypeError."""
    matrix1 = [[1, 2], [3, 4]]
    matrix2 = "not a matrix"
    with pytest.raises(TypeError, match="Inputs must be lists"):
        add_matrices(matrix1, matrix2)

def test_non_list_rows_raises_error():
    """Test that non-list rows raise a TypeError."""
    matrix1 = [[1, 2], 3]
    matrix2 = [[1, 2], [3, 4]]
    with pytest.raises(TypeError, match="Matrix rows must be lists"):
        add_matrices(matrix1, matrix2)