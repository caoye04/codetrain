# medium
# 23. 排序数组找元素第一个和最后一个位置
# 给你一个按照非递减顺序排列的整数数组 nums，和一个目标值 target。请你找出给定目标值在数组中的开始位置和结束位置。
# 如果数组中不存在目标值 target，返回 [-1, -1]。
# 你必须设计并实现时间复杂度为 O(log n) 的算法解决此问题。

nums = list(map(int,input().strip().split()))
target = int(input())

def searchLeft():
    l,r = 0, len(nums)-1
    while l<=r:
        mid = (r-l)//2+l
        if nums[mid] == target:
            if mid==0 or nums[mid-1]<target:
                return mid
            else:
                r = mid-1
        elif nums[mid] < target:
            l = mid+1
        else :
            r =mid-1
    return -1

def searchRight():
    l,r = 0, len(nums)-1
    while l<=r:
        mid = (r-l)//2+l
        if nums[mid] == target:
            if mid==len(nums)-1 or nums[mid+1]>target:
                return mid
            else:
                r = mid-1
        elif nums[mid] < target:
            l = mid+1
        else :
            r =mid-1
    return -1

print([searchLeft(),searchRight()])
    