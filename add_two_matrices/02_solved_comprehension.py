
a = [[1, -2], [-3, 4]]
b = [[2, -1], [0, -1]]

output = [ [ a[i][j] + b[i][j] for j in range(len(a[0])) ] for i in range(len(a))]

# [[3, -3], [-3, 3]]