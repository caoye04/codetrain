# # Friend
# **时间限制：** 1.0 秒
# **空间限制：** 512 MB
# ## 题目描述
# F 学校有 $n$ 个学生，编号为 $1, 2, \cdots, n$。这些学生之间存在 $m$ 对好友关系。每对好友关系形如：$u_j$ 号学生与 $v_j$ 号学生互为好友 $(1 \le j \le m)$。好友关系是双向的，这意味着 $u_j$ 号学生是 $v_j$ 号学生的好友，同时 $v_j$ 号学生也是 $u_j$ 号学生的好友。
# F 学校要将 $n$ 个学生均匀（等概率）随机地分为若干小组，每组 3 个学生。保证 $n$ 是 3 的倍数，即能够恰好分完。在分组完毕后，每个组内的好友关系也会有不同的情况。现在，对于每个学生 $i$，他希望计算他所在小组的 3 个学生当中以下每个事件发生的概率：
# 1. 3 个学生两两均不为好友；
# 1. 3 个学生中，除自己外的 2 个学生互为好友，不存在其他好友关系；
# 1. 3 个学生中，自己与另外某个学生互为好友，不存在其他好友关系；
# 1. 3 个学生中，恰好有 2 对好友关系，且有 2 个好友的那个人是自己（即：自己与另外 2 个学生分别互为好友，但他们两个不为好友）；
# 1. 3 个学生中，恰好有 2 对好友关系，但有 2 个好友的那个人不是自己（即：存在某个学生 A 与自己和另外一个学生 B（分别）互为好友，但自己与 B 不为好友）；
# 1. 3 个学生中两两互为好友。
# 请帮助每个学生计算吧！

# ## 输入格式
# 从标准输入读入数据。
# 第一行输入两个正整数 $n, m$，以空格隔开。
# 接下来 $m$ 行，每行输入两个正整数 $u_j, v_j(u_j\ne v_j)$，以空格隔开，表示 $u_j$ 与 $v_j$ 号学生互为好友。
# 数据保证不存在两组重复的好友关系。
# ## 输出格式
# 输出到标准输出。
# 输出 $n$ 行，每行 6 个最简分数，以空格隔开，表示每个学生每种情况的发生概率。
# 输出最简分数的形式为：先输出分子，再输出斜线 $/$，最后输出分母。你应当输出最简分数，例如不应当输出 $3/6$，而应输出 $1/2$ 。
# 特殊地，如果所求的某个概率为 $0$，应当输出 $0/1$；概率为 $1$ 则输出 $1/1$ 。
# ## 样例 1 输入
# 3 2
# 1 2
# 1 3
# ## 样例 1 输出
# 0/1 0/1 0/1 1/1 0/1 0/1
# 0/1 0/1 0/1 0/1 1/1 0/1
# 0/1 0/1 0/1 0/1 1/1 0/1
# ## 样例 1 解释
# 一共只有 3 个学生，分组实际上仅有一种方案，不存在随机性。
# 3 个学生之间存在 2 对好友关系，在 1 号学生看来是第 4 种情况，在 2 号和 3 号学生看来是第 5 种情况。
# ## 样例 2 输入
# 6 6
# 1 2
# 2 3
# 3 1
# 1 4
# 1 5
# 1 6
# ## 样例 2 输出
# 0/1 0/1 0/1 9/10 0/1 1/10
# 3/10 0/1 3/10 0/1 3/10 1/10
# 3/10 0/1 3/10 0/1 3/10 1/10
# 1/2 1/10 0/1 0/1 2/5 0/1
# 1/2 1/10 0/1 0/1 2/5 0/1
# 1/2 1/10 0/1 0/1 2/5 0/1

from fractions import Fraction
from itertools import combinations
import math

def solve():
    n, m = map(int, input().split())
    
    # 构建好友关系图
    friends = [set() for _ in range(n + 1)]
    for _ in range(m):
        u, v = map(int, input().split())
        friends[u].add(v)
        friends[v].add(u)
    
    # 生成所有可能的3人组合
    all_students = list(range(1, n + 1))
    all_groups = list(combinations(all_students, 3))
    
    # 计算总的分组方案数
    # 这是一个复杂的组合数学问题，需要计算将n个人分成n/3个3人组的方案数
    total_ways = calculate_total_grouping_ways(n)
    
    # 为每个学生初始化6种情况的计数
    student_counts = [[0] * 6 for _ in range(n + 1)]
    
    # 为每个学生计算他参与的所有可能3人组
    for student in range(1, n + 1):
        # 找到包含该学生的所有3人组
        student_groups = [group for group in all_groups if student in group]
        
        # 计算该学生被分到每个组的概率权重
        for group in student_groups:
            a, b, c = group
            
            # 计算这个特定3人组在所有分组方案中出现的次数
            group_weight = calculate_group_weight(group, n)
            
            # 判断这个组属于哪种情况（从学生的视角）
            case = classify_group(student, group, friends)
            
            # 累加到对应情况的计数中
            student_counts[student][case] += group_weight
    
    # 输出结果
    for student in range(1, n + 1):
        results = []
        for case in range(6):
            prob = Fraction(student_counts[student][case], total_ways)
            results.append(f"{prob.numerator}/{prob.denominator}")
        print(" ".join(results))

def calculate_total_grouping_ways(n):
    """计算将n个人分成n/3个3人组的总方案数"""
    groups = n // 3
    # 公式：n! / (3!^(n/3) * (n/3)!)
    numerator = math.factorial(n)
    denominator = (math.factorial(3) ** groups) * math.factorial(groups)
    return numerator // denominator

def calculate_group_weight(group, n):
    """计算特定3人组在所有分组方案中出现的次数"""
    remaining = n - 3
    if remaining == 0:
        return 1
    # 剩余remaining个人分成remaining/3个3人组的方案数
    remaining_groups = remaining // 3
    numerator = math.factorial(remaining)
    denominator = (math.factorial(3) ** remaining_groups) * math.factorial(remaining_groups)
    return numerator // denominator

def classify_group(student, group, friends):
    """判断3人组从指定学生视角属于哪种情况"""
    a, b, c = group
    
    # 重新排列，让student在第一位
    if student == a:
        me, other1, other2 = a, b, c
    elif student == b:
        me, other1, other2 = b, a, c
    else:  # student == c
        me, other1, other2 = c, a, b
    
    # 统计好友关系
    me_other1 = other1 in friends[me]
    me_other2 = other2 in friends[me]
    other1_other2 = other2 in friends[other1]
    
    total_friendships = sum([me_other1, me_other2, other1_other2])
    
    if total_friendships == 0:
        return 0  # 情况1：无好友关系
    elif total_friendships == 1:
        if other1_other2:
            return 1  # 情况2：除自己外的2人是好友
        else:
            return 2  # 情况3：自己与某人是好友
    elif total_friendships == 2:
        if me_other1 and me_other2:
            return 3  # 情况4：自己有2个好友
        else:
            return 4  # 情况5：别人有2个好友
    else:  # total_friendships == 3
        return 5  # 情况6：两两都是好友

# 简化版本（适用于小规模数据）
def solve_simple():
    """适用于n较小的情况，直接枚举所有分组方案"""
    n, m = map(int, input().split())
    
    friends = [set() for _ in range(n + 1)]
    for _ in range(m):
        u, v = map(int, input().split())
        friends[u].add(v)
        friends[v].add(u)
    
    students = list(range(1, n + 1))
    all_groupings = generate_all_groupings(students)
    
    # 为每个学生统计6种情况的出现次数
    counts = [[0] * 6 for _ in range(n + 1)]
    
    for grouping in all_groupings:
        for group in grouping:
            for student in group:
                case = classify_group(student, group, friends)
                counts[student][case] += 1
    
    total_groupings = len(all_groupings)
    
    for student in range(1, n + 1):
        results = []
        for case in range(6):
            prob = Fraction(counts[student][case], total_groupings)
            results.append(f"{prob.numerator}/{prob.denominator}")
        print(" ".join(results))

def generate_all_groupings(students):
    """生成所有可能的分组方案（递归）"""
    if len(students) == 0:
        return [[]]
    if len(students) == 3:
        return [[tuple(students)]]
    
    result = []
    first = students[0]
    remaining = students[1:]
    
    # 选择first的两个伙伴
    for i in range(len(remaining)):
        for j in range(i + 1, len(remaining)):
            partner1, partner2 = remaining[i], remaining[j]
            current_group = (first, partner1, partner2)
            
            # 剩余的学生
            rest = [s for s in remaining if s != partner1 and s != partner2]
            
            # 递归处理剩余学生
            sub_groupings = generate_all_groupings(rest)
            
            for sub_grouping in sub_groupings:
                result.append([current_group] + sub_grouping)
    
    return result

if __name__ == "__main__":
    solve_simple()  # 对于比赛，可能需要根据数据规模选择不同的实现