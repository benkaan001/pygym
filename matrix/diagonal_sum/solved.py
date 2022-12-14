# Given the 4x4 matrix m, print the diagonal sum,
# Expected output: 1 + 30 + 500 + 7000 = 7531

"""

[[1, 3, 5, 7],
[10, 30, 50, 70],
[100, 300, 500, 700],
[1000, 3000, 5000, 7000]]

"""

m = [[1, 3, 5, 7], [10, 30, 50, 70], [100, 300, 500, 700], [1000, 3000, 5000, 7000]]

sum_left = 0

for i in range(len(m)):
    for j in range(len(m[i])):
        if j == i:
            sum_left += m[j][i]
            print(sum_left, end=" -> ")  # 1 -> 31 -> 531 -> 7531


sum_rigth = 0

for i in range(len(m)):
    for j in range(len(m[i])):
        if j == len(m) - i - 1:
            sum_rigth += m[i][j]
            print(sum_rigth, end="-> ")  # 7-> 57-> 357-> 1357
