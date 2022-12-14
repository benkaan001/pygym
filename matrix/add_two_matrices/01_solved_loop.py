def add(matrix1, matrix2):
    output = []
    for i in range(len(matrix1)):
        temp = []
        for j in range(len(matrix1[i])):
            total = matrix1[i][j] + matrix2[i][j]
            temp.append(total)
        output.append(temp)
    
    return output


        
matrix1 =[[1, -2, 3], [-4, 5, -6], [7, -8, 9]]
matrix2 =[[1, 1, 0], [1, -2, 3], [-2, 2, -2]]

print(add(matrix1, matrix2))
# [[2, -1, 3], [-3, 3, -3], [5, -6, 7]]

"""
matrix1 = [[1, -2, 3], [-4, 5, -6], [7, -8, 9]] | matrix2 = [[1, 1, 0], [1, -2, 3], [-2, 2, -2]] 
output = [] 
i = 0                                           | i = 1                                             | i = 2 
temp = []                                       | temp = []                                         | temp = [] 
j = 0      | j = 1          | j = 2             | j = 0       | j = 1          | j = 2              | j = 0      | j = 1          | j = 2 
total = 2  | total = -1     | total = 3         | total = -3  | total = 3      | total = -3         | total = 5  | total = -6     | total = 7 
temp = [2] | temp = [2, -1] | temp = [2, -1, 3] | temp = [-3] | temp = [-3, 3] | temp = [-3, 3, -3] | temp = [5] | temp = [5, -6] | temp = [5, -6, 7] 
output = [[2, -1, 3]]                           | output = [[2, -1, 3], [-3, 3, -3]]                | output = [[2, -1, 3], [-3, 3, -3], [5, -6, 7]]

"""