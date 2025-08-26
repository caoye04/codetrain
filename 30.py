# # 任务调度

# **时间限制：** 3.0 秒

# **空间限制：** 512 MB

# ## 题目描述

# 任务调度是计算机系统中一项重要的工作。今天你的任务，就是模拟一个计算机系统模型的任务调度过程，并给出相应操作的执行结果。

# 在这个模型中，不同任务按照一定顺序到来，等待被执行。任务处理机制需要维护任务的等待情况，并在相应的时机选择相应的任务进行执行。

# 不同的任务之间以编号进行区分，为方便起见，按照任务到来的顺序，由先到后编号为 $1,2,3,...$ 。每个任务都拥有一个重要程度 $a_i$ ，所有任务的重要程度两两不同。

# 在一般情况下，处理任务应当按照任务到来的先后顺序依次处理，也就是说任务等待应当形成一个队列。但考虑到不同任务的重要程度不同，这一原则可能被打破。具体而言，有如下几种操作：

# - $1\text{ }a_i$ : 一个新的任务到来，其编号为先前出现过的最大任务编号 $+1$ ，其重要程度为 $a_i$，在任务等待队列中被安排至队列末尾。考虑到计算机内存限制，同一时刻正在等待的任务数量不能超过 $m$ ，因此如果当前已经有 $m$ 个任务在等待，则这一操作将出现错误。
# - $2\text{ }a_i\text{ }x_i$ : 一个新的任务到来，其编号为先前出现过的最大任务编号 $+1$ ，其重要程度为 $a_i$，在任务等待队列中被安排至任务编号为 $x_i$ 的任务前面并紧挨任务 $x_i$ 的位置。如果当前已有 $m$ 个任务在等待，或任务 $x_i$ 当前不在等待队列中，这一操作将出现错误。
# - $3$ : 任务处理机制将处理当前排在等待队列队首的任务，并将其从等待队列中移除。若当前等待队列为空，这一操作将出现错误。
# - $4$ : 任务处理机制将处理当前等待队列中重要程度最大的任务，并将其从等待队列中移除。若当前等待队列为空，这一操作将出现错误。

# 除上述提到的错误情况外，操作均可以成功执行。

# 最开始，任务等待队列为空，接下来你需要处理 $n$ 个操作，每个操作形如上述几种之一。对于每个操作，你需要正确判断是否会出现错误，如果出现错误，需要输出一个 `ERR` ，并不予以执行（但对于操作 $1$ 和 $2$ 而言，仍会占用一个新的任务编号）；如果可以成功执行，则需要输出一个正整数，表示这次操作涉及到的任务编号，在操作 $1$ 和 $2$ 中表示新到来的任务编号，操作 $3$ 和 $4$ 中表示被处理的任务编号。

# ## 输入格式

# 从标准输入读入数据。

# 输入的第一行包含两个正整数 $n, m$ ，分别表示需要执行的操作个数和队伍的最大容量。

# 接下来 $n$ 行，每行按上述格式描述一个操作。

# ## 输出格式

# 输出到标准输出。

# 输出 $n$ 行，每行表示对应操作执行的结果，格式如上所述。

# ## 样例 1 输入

# ```
# 12 3
# 1 2
# 1 6
# 2 1 2
# 2 7 3
# 1 5
# 3
# 3
# 1 8
# 2 4 3
# 4
# 4
# 4
# ```

# ## 样例 1 输出

# ```
# 1
# 2
# 3
# ERR
# ERR
# 1
# 3
# 6
# ERR
# 6
# 2
# ERR
# ```

# ## 样例 1 解释

# 第 $4, 5$ 次操作均因等待队列已满而出现错误，第 $9$ 次操作因 $x_i$ 不存在于等待队列中而出现错误，第 $12$ 次操作因等待队列为空而出现错误。

from collections import deque

def solve():
    n, m = map(int, input().split())
    
    # 任务等待队列，存储任务编号
    queue = deque()
    # 任务重要程度字典
    importance = {}
    # 当前最大任务编号
    max_task_id = 0
    
    for _ in range(n):
        operation = list(map(int, input().split()))
        
        if operation[0] == 1:  # 操作1：队尾添加任务
            a_i = operation[1]
            
            if len(queue) >= m:  # 队列已满
                max_task_id += 1  # 仍要占用编号
                print("ERR")
            else:
                max_task_id += 1
                queue.append(max_task_id)
                importance[max_task_id] = a_i
                print(max_task_id)
                
        elif operation[0] == 2:  # 操作2：在指定任务前插入
            a_i = operation[1]
            x_i = operation[2]
            
            if len(queue) >= m or x_i not in queue:  # 队列已满或目标任务不存在
                max_task_id += 1  # 仍要占用编号
                print("ERR")
            else:
                max_task_id += 1
                # 找到x_i的位置，在其前面插入
                queue_list = list(queue)
                insert_pos = queue_list.index(x_i)
                queue_list.insert(insert_pos, max_task_id)
                queue = deque(queue_list)
                importance[max_task_id] = a_i
                print(max_task_id)
                
        elif operation[0] == 3:  # 操作3：处理队首任务
            if len(queue) == 0:  # 队列为空
                print("ERR")
            else:
                task_id = queue.popleft()
                del importance[task_id]
                print(task_id)
                
        elif operation[0] == 4:  # 操作4：处理重要程度最高的任务
            if len(queue) == 0:  # 队列为空
                print("ERR")
            else:
                # 找到重要程度最高的任务
                max_importance = -1
                max_task = -1
                for task_id in queue:
                    if importance[task_id] > max_importance:
                        max_importance = importance[task_id]
                        max_task = task_id
                
                # 从队列中移除该任务
                queue.remove(max_task)
                del importance[max_task]
                print(max_task)

solve()