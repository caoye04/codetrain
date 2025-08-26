# # 公司
# **时间限制：** 1.0 秒
# **空间限制：** 512 MB
# ## 题目描述
# 给定一个有 $n$ 个雇员的初创公司，雇员从 $1$ 到 $n$ 编号，编号为 $i$ 的人有一个固定的薪资 $a_i$ 。最初所有人都不知道公司里其他员工的薪资。
# 某一天由于公司数据库发生问题，泄露了 $m$ 条数据，导致有一部分人知道了其他部分人的薪资。其中对于编号为 $i$ 的雇员，设他所了解到的人的平均薪资为 $v_i$ （如果有多条重复的数据，那么也会被计算多次），如果 $a_i<v_i$ 那么他就会萌生想要离职的想法。
# 当然如果一个人不了解其他人的薪资，那么他也不会萌生想要离职的想法。
# 给定所有 $n$ 个人的薪资 $a_i$ ，以及 $m$ 个数对 $(x_i,y_i)$ 表示编号为 $x_i$ 的雇员知道了编号为 $y_i$ 的雇员的薪资，问会有多少雇员萌生离职的想法。
# ## 输入格式
# 从标准输入读入数据。
# 输入的第一行包含两个正整数 $n,m$ , 分别表示公司的人数和泄露的数据条数。
# 输入的第二行包含 $n$ 个正整数 $a_i$ , 依次表示 $n$ 个人的薪资。
# 接下来 $m$ 行，每行包含两个正整数 $(x_i,y_i)$ 表示编号为 $x_i$ 的雇员知道了编号为 $y_i$ 雇员的薪资。
# ## 输出格式
# 输出到标准输出。
# 输出一个正整数表示对应的答案。
# ## 样例 1 输入
# 4 4
# 10 20 30 40
# 3 2
# 3 4
# 3 4
# 1 2
# ## 样例 1 输出
# 2
# ## 样例 1 解释
# 编号为 $1$ 和 $3$ 的雇员都会萌生离职的想法。
from collections import defaultdict

n,m = map(int, input().split())
salary = list(map(int,input().strip().split()))
secret = defaultdict(list)
result = 0

for i in range(m):
    k,l = map(int,input().split())
    secret[k].append(salary[l-1])

for i in range(n):
    if secret[i+1]:
        sum = 0
        num = 0
        for item in secret[i+1]:
            sum += item
            num += 1
        avr_salary = sum/num
        if avr_salary > salary[i]:
            result += 1

print(result)