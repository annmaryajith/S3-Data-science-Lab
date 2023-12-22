import numpy as np
def input_matrix(matrix_name):
    rows = int(input(f"Enter the no of rows of {matrix_name}: "))
    cols = int(input(f"Enter the no of columns of {matrix_name}: "))
    matrix=[]
    print("Enter the elements:")
    for i in range(rows):
        rows=[]
        for j in range(cols):
            element=int(input(f"Enter the element at row {i+1},column {j+1}:"))
            rows.append(element)
        matrix.append(rows)
    return np.array(matrix)
matrix1 = input_matrix("matrix1")
matrix2 = input_matrix("matrix2")
sum = np.add(matrix1, matrix2)
print("Addition=", sum)
diff = np.subtract(matrix1, matrix2)
print("Subtraction=", diff)
prod = np.multiply(matrix1, matrix2)
print("Multiplication=", prod)
div = np.divide(matrix1, matrix2)
print("Division=", div)
transp = np.transpose(matrix1)
print("Transpose=", transp)
dot = np.dot(matrix1, matrix2)
print("Dot product=", dot)


