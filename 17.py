# medium
# 搜索二维矩阵
# 编写一个高效的算法来搜索 m x n 矩阵 matrix 中的一个目标值 target 。该矩阵具有以下特性：
# 每行的元素从左到右升序排列。
# 每列的元素从上到下升序排列。

# 输入：matrix = [[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]], target = 5
# 输出：true

# 输入：matrix = [[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]], target = 20
# 输出：false

def searchMatrix(matrix: list[list[int]], target: int) -> bool:
    i = len(matrix) - 1
    j = 0
    while j < len(matrix[0]) and i >= 0:
        # print([i,j])
        if matrix[i][j] == target:
            return True
        elif matrix[i][j] > target:
            i -= 1
        elif matrix[i][j] < target:
            j += 1
    return False

m = int(input())
matrix = list(list())
for i in range(m):
    nums = list(map(int,input().strip().split()))
    matrix.append(nums)
target = int(input())
print(searchMatrix(matrix,target))
