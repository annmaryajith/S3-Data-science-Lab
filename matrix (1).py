import numpy as np
def input_matrix():
    rows = int(input("Enter the no of rows:"))
    cols = int(input("Enter the no of columns:"))
    matrix=[]
    print("Enter the elements:")
    for i in range(rows):
        for j in range(cols):
            element=int(input(f"Enter the element at row {i+1},column {j+1}:"))
            rows.append(element)
            matrix.append(rows)
return np.array(matrix)


