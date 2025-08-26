# medium
# 20.岛屿数量
# 给你一个由 '1'（陆地）和 '0'（水）组成的的二维网格，请你计算网格中岛屿的数量。
# 岛屿总是被水包围，并且每座岛屿只能由水平方向和/或竖直方向上相邻的陆地连接形成。
# 此外，你可以假设该网格的四条边均被水包围。

#  输入：grid = [
#   ["1","1","1","1","0"],
#   ["1","1","0","1","0"],
#   ["1","1","0","0","0"],
#   ["0","0","0","0","0"]
# ]
# 输出：1

# 输入：grid = [
#   ["1","1","0","0","0"],
#   ["1","1","0","0","0"],
#   ["0","0","1","0","0"],
#   ["0","0","0","1","1"]
# ]
# 输出：3

def solution(grid):
    def dfs(grid,i,j):
        if not 0<=i<len(grid) or not 0<=j<len(grid[0]) or grid[i][j]==0:
            return
        grid[i][j] = 0
        dfs(grid, i + 1, j)
        dfs(grid, i, j + 1)
        dfs(grid, i - 1, j)
        dfs(grid, i, j - 1)
    res = 0
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == 1:
                dfs(grid,i,j)
                res += 1
    return res

grid = list(list())
m = int(input())
for i in range(m):
    nums = list(map(int,input().strip().split()))
    grid.append(nums)
print(solution(grid))