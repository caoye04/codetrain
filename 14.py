# medium
# 14.矩阵置零
# 给定一个 m x n 的矩阵，如果一个元素为 0 ，则将其所在行和列的所有元素都设为 0 。请使用 原地 算法。
# 输入：matrix = [[1,1,1],[1,0,1],[1,1,1]]
# 输出：[[1,0,1],[0,0,0],[1,0,1]]
# 输入：matrix = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]
# 输出：[[0,0,0,0],[0,4,5,0],[0,3,1,0]]

m = int(input())
n = int(input())
matrix = list(list())
for i in range(n):
    nums = list(map(int,input().strip().split()))
    matrix.append(nums)
flag_row1_have0 = 0
for item in matrix[0]:
    if item == 0:
        flag_row1_have0 = 1
for row in range(1,len(matrix)):
    flag = 0
    for i in range(len(matrix[row])):
        if matrix[row][i] == 0:
            matrix[0][i] = 0
            flag = 1
    if flag == 1:
        for i in range(len(matrix[row])):
            matrix[row][i] = 0
# print(matrix)
for i in range(len(matrix[0])):
    if matrix[0][i]==0:
        for j in range(len(matrix)):
            matrix[j][i] = 0
# print(matrix)
if flag_row1_have0 == 1:
    for i in range(len(matrix[0])):
        matrix[0][i] = 0

print(matrix)
