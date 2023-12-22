import numpy as np
matrix= np.array([[5,6,4],
                  [2,5,6],
                  [3,5,6]])
U,S,VT =np.linalg.svd(matrix)
print("U=")
print(U)
print("S=")
print(np.diag(S))
print("VT=")
print(VT)

reconstructed_matrix= np.dot(U, np.dot(np.diag(S), VT))
print("Reconstructed matrix=")
print(reconstructed_matrix)