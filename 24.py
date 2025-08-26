# medium
# 24.每日温度
# 给定一个整数数组 temperatures ，表示每天的温度，返回一个数组 answer ，其中 answer[i] 是指对于第 i 天，下一个更高温度出现在几天后。如果气温在这之后都不会升高，请在该位置用 0 来代替。
# 输入: temperatures = [73,74,75,71,69,72,76,73]
# 输出: [1,1,4,2,1,1,0,0]
# 输入: temperatures = [30,40,50,60]
# 输出: [1,1,1,0]
# 输入: temperatures = [30,60,90]
# 输出: [1,1,0]

nums = list(map(int, input().strip().split()))

def daily_temperatures(temperatures):
    n = len(temperatures)
    result = [0] * n  # 初始化结果数组，默认都是0
    stack = []  # 单调栈，存储索引
    
    for i in range(n):
        # 当栈不为空且当前温度大于栈顶索引对应的温度时
        while stack and temperatures[i] > temperatures[stack[-1]]:
            prev_index = stack.pop()  # 弹出栈顶索引
            result[prev_index] = i - prev_index  # 计算距离
        
        stack.append(i)  # 将当前索引入栈
    
    return result

# 调用函数并输出结果
answer = daily_temperatures(nums)
print(answer)