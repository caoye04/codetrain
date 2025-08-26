# # 等差数列
# **时间限制：** 1.0 秒
# **空间限制：** 512 MB
# ## 题目描述
# 有一个特殊的 $n$ 行 $m$ 列的矩阵 $A_{ij}~(1 \le i \le n,~1 \le j \le m)$，每个元素都是正整数，每一行和每一列都是独立的等差数列。在某一次故障中，这个矩阵的某些元素的真实值丢失了，被重置为 $0$。现在需要你想办法恢复这些元素，并且按照行号和列号从小到大的顺序（行号为第一关键字，列号为第二关键字，从小到大）输出能够恢复的元素。
# ## 输入格式
# 从标准的输入读入数据。
# 输入的第一行包含两个正整数 $n$ 和 $m$，保证 $n \le 10^3$ 和 $m \le 10^3$ 。
# 接下来 $n$ 行，每行 $m$ 个整数，表示整个矩阵，保证 $1 \le A_{ij} \le 10^9$。如果 $A_{ij}$ 等于 $0$，表示真实值丢失的元素。
# ## 输出格式
# 输出到标准输出。
# 输出若干行，表示所有能够恢复的元素。每行三个整数 $i,j,x$，表示 $A_{ij}$ 的真实值是 $x$ 。
# ## 样例 1 输入
# 3 4
# 1 2 0 0
# 0 0 0 0
# 3 0 0 0
# ## 样例 1 输出
# 1 3 3
# 1 4 4
# 2 1 2
# ## 样例 1 解释
# 可以恢复 $3$ 个元素，$A_{13}$ 的真实值是 $3$，$A_{14}$ 的真实值是 $4$，$A_{21}$ 的真实值是 $2$ 。

# 读取输入
n, m = map(int, input().split())
matrix = []
original_matrix = []  # 保存原始矩阵用于判断哪些是恢复的
for i in range(n):
    nums = list(map(int, input().strip().split()))
    matrix.append(nums[:])  # 工作矩阵
    original_matrix.append(nums[:])  # 原始矩阵

# 存储每行每列的等差数列信息
hang_info = {}  # 行信息: {行号: (首项, 公差)}
lie_info = {}   # 列信息: {列号: (首项, 公差)}

def get_arithmetic_info(arr):
    """从数组中获取等差数列信息，返回(首项, 公差)或None"""
    non_zero = [(i, val) for i, val in enumerate(arr) if val != 0]
    
    if len(non_zero) < 2:
        return None
    
    # 用前两个非零元素计算公差
    pos1, val1 = non_zero[0]
    pos2, val2 = non_zero[1]
    
    if pos2 == pos1:
        return None
    
    d = (val2 - val1) // (pos2 - pos1)
    a1 = val1 - d * pos1
    
    # 验证所有非零元素是否符合等差数列
    for pos, val in non_zero:
        if a1 + d * pos != val:
            return None
    
    if a1 <= 0:  # 确保首项为正
        return None
        
    return (a1, d)

# 反复尝试恢复，直到无法继续
changed = True
while changed:
    changed = False
    
    # 尝试确定每行的等差数列信息
    for i in range(n):
        if i not in hang_info:
            info = get_arithmetic_info(matrix[i])
            if info:
                hang_info[i] = info
                # 用等差数列信息填充该行的0
                a1, d = info
                for j in range(m):
                    if matrix[i][j] == 0:
                        matrix[i][j] = a1 + d * j
                        changed = True
    
    # 尝试确定每列的等差数列信息
    for j in range(m):
        if j not in lie_info:
            col = [matrix[i][j] for i in range(n)]
            info = get_arithmetic_info(col)
            if info:
                lie_info[j] = info
                # 用等差数列信息填充该列的0
                a1, d = info
                for i in range(n):
                    if matrix[i][j] == 0:
                        matrix[i][j] = a1 + d * i
                        changed = True

# 收集并输出恢复的元素
results = []
for i in range(n):
    for j in range(m):
        if original_matrix[i][j] == 0 and matrix[i][j] != 0:
            results.append((i+1, j+1, matrix[i][j]))

# 按行号和列号排序输出
results.sort()
for i, j, x in results:
    print(i, j, x)