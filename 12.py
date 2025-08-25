# medium
# 12.轮转数组
# 给定一个整数数组 nums，将数组中的元素向右轮转 k 个位置，其中 k 是非负数。
# 输入: nums = [1,2,3,4,5,6,7], k = 3
# 输出: [5,6,7,1,2,3,4]
# 输入：nums = [-1,-100,3,99], k = 2
# 输出：[3,99,-1,-100]

nums = list(map(int,input().strip().split()))
k = int(input())
n = k % len(nums)
nums[:]=nums[-n:]+nums[:-n]
print(nums)