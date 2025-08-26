# 往年题
# 统计次数
# **时间限制：** 1.0 秒
# **空间限制：** 512 MB
# ## 题目描述
# 给定两个正整数 $n$ 和 $k~(1 \le k \le 9)$，求从 1 到 $n$ 这 $n$ 个正整数的十进制表示中 $k$ 出现的次数。
# ## 输入格式
# 从标准输入读入数据。
# 输入的第一行包含两个正整数 $n$ 和 $k$，保证 $n \le 10^6$ 和 $1 \le k \le 9$ 。
# ## 输出格式
# 输出到标准输出。
# 输出一个整数，表示答案。
# ## 样例 1 输入
# 12 1
# ## 样例 1 输出
# 5
# ## 样例 1 解释
# 从 $1$ 到 $12$ 这些整数中包含 $1$ 的数字有 $1,10,11,12$，一共出现了 $5$ 次 $1$ 。

# import time
# start_time = time.perf_counter()

# n, k = map(int, input().split())
# count = 0
# k_str = str(k)

# for i in range(1, n + 1):
#     count += str(i).count(k_str)

# print(count)

# end_time = time.perf_counter()
# print(f"执行时间: {end_time - start_time:.4f} 秒")

import time

def count_digit_fast(n, k):
    if n <= 0:
        return 0
    
    s = str(n)
    length = len(s)
    count = 0
    
    for i in range(length):
        # 当前位左边的数字
        left = int(s[:i]) if i > 0 else 0
        # 当前位的数字  
        cur = int(s[i])
        # 当前位右边的数字个数
        right_count = length - i - 1
        # 当前位的权重
        power = 10 ** right_count
        
        if cur < k:
            count += left * power
        elif cur == k:
            right = int(s[i+1:]) if i < length - 1 else 0
            count += left * power + right + 1
        else:  # cur > k
            count += (left + 1) * power
    
    return count

start_time = time.perf_counter()

n, k = map(int, input().split())
result = count_digit_fast(n, k)
print(result)

end_time = time.perf_counter()
print(f"执行时间: {end_time - start_time:.6f} 秒")