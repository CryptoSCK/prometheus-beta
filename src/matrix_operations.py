"""
Matrix operations module providing matrix addition functionality.

This module includes a function for adding two matrices with 
comprehensive error checking for matrix compatibility.
"""

def add_matrices(matrix1, matrix2):
    """
    Add two matrices element-wise with size compatibility checking.

    Args:
        matrix1 (list of lists): First input matrix 
        matrix2 (list of lists): Second input matrix

    Returns:
        list of lists: A new matrix containing the element-wise sum

    Raises:
        TypeError: If inputs are not lists or contain non-numeric elements
        ValueError: If matrices have incompatible dimensions
    """
    # Check input types
    if not (isinstance(matrix1, list) and isinstance(matrix2, list)):
        raise TypeError("Inputs must be lists")
    
    # Check for empty matrices
    if not matrix1 or not matrix2:
        raise ValueError("Matrices cannot be empty")
    
    # Check row consistency in each matrix
    if any(not isinstance(row, list) for row in matrix1 + matrix2):
        raise TypeError("Matrix rows must be lists")
    
    # Check matrix dimensions
    if len(matrix1) != len(matrix2):
        raise ValueError("Matrices must have the same number of rows")
    
    # Check that all rows in each matrix have consistent length
    if any(len(row) != len(matrix1[0]) for row in matrix1) or \
       any(len(row) != len(matrix2[0]) for row in matrix2):
        raise ValueError("All rows in each matrix must have the same length")
    
    # Check matrix column compatibility 
    if len(matrix1[0]) != len(matrix2[0]):
        raise ValueError("Matrices must have the same number of columns")
    
    # Check that all elements are numeric
    def is_numeric(value):
        return isinstance(value, (int, float))
    
    if not all(is_numeric(elem) for row in matrix1 + matrix2 for elem in row):
        raise TypeError("Matrix elements must be numeric")
    
    # Perform matrix addition
    result = []
    for i in range(len(matrix1)):
        row = []
        for j in range(len(matrix1[0])):
            row.append(matrix1[i][j] + matrix2[i][j])
        result.append(row)
    
    return result