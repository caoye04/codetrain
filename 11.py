# medium
# 11. 合并区间
# 以数组 intervals 表示若干个区间的集合，其中单个区间为 intervals[i] = [starti, endi] 。请你合并所有重叠的区间，并返回 一个不重叠的区间数组，该数组需恰好覆盖输入中的所有区间 。
# 输入：intervals = [[1,3],[2,6],[8,10],[15,18]]
# 输出：[[1,6],[8,10],[15,18]]
# 输入：intervals = [[1,4],[4,5]]
# 输出：[[1,5]]

def s11(intervals):
    intervals.sort(key=lambda p:p[0])
    ans = []
    for p in intervals:
        if ans and p[0] <= ans[-1][1]:
            ans[-1][1] = max(ans[-1][1],p[1])
        else:
            ans.append(p)
    return ans

intervals = []
while True:
    nums = list(map(int,input().strip().split()))
    if nums == []:
        break
    intervals.append(nums)
ans = s11(intervals)
print(ans)

