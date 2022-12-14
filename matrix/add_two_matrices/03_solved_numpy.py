import numpy as np

a = [[1, -2], [-3, 4]]
b = [[2, -1], [0, -1]]

matrix1 = np.matrix(a) # matrix1 = matrix([[ 1, -2], [-3, 4]])  
matrix2 = np.matrix(b) # matrix2 = matrix([[ 2, -1], [ 0, -1]]) 

print(matrix1 + matrix2) # [[ 3 -3]\n [-3  3]]