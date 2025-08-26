# medium
# 21.腐烂的橘子
# 在给定的 m x n 网格 grid 中，每个单元格可以有以下三个值之一：
# 值 0 代表空单元格；
# 值 1 代表新鲜橘子；
# 值 2 代表腐烂的橘子。
# 每分钟，腐烂的橘子 周围 4 个方向上相邻 的新鲜橘子都会腐烂。
# 返回 直到单元格中没有新鲜橘子为止所必须经过的最小分钟数。如果不可能，返回 -1 。

# 输入：grid = [[2,1,1],[1,1,0],[0,1,1]]
# 输出：4
# 输入：grid = [[2,1,1],[0,1,1],[1,0,1]]
# 输出：-1
# 输入：grid = [[0,2]]
# 输出：0

from collections import deque

def orangesRotting(grid):
    if not grid or not grid[0]:
        return 0
    
    rows, cols = len(grid), len(grid[0])
    queue = deque()
    fresh_count = 0
    
    # 找到所有腐烂橘子的位置，统计新鲜橘子数量
    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == 2:
                queue.append((i, j))
            elif grid[i][j] == 1:
                fresh_count += 1
    
    # 如果没有新鲜橘子，直接返回0
    if fresh_count == 0:
        return 0
    
    # 四个方向：上、下、左、右
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    minutes = 0
    
    # BFS模拟腐烂过程
    while queue:
        size = len(queue)
        has_rotted = False
        
        # 处理当前这一轮的所有腐烂橘子
        for _ in range(size):
            x, y = queue.popleft()
            
            # 向四个方向传播
            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                
                # 检查边界和是否为新鲜橘子
                if 0 <= nx < rows and 0 <= ny < cols and grid[nx][ny] == 1:
                    grid[nx][ny] = 2  # 变腐烂
                    queue.append((nx, ny))
                    fresh_count -= 1
                    has_rotted = True
        
        # 如果这一轮有橘子腐烂，时间+1
        if has_rotted:
            minutes += 1
    
    # 如果还有新鲜橘子剩余，返回-1
    return minutes if fresh_count == 0 else -1

m = int(input())
grid = list(list())
for i in range(m):
    nums = list(map(int,input().strip().split()))
    grid.append(nums)
print(orangesRotting(grid))
