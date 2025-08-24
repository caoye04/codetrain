# medium
# 6. 三数之和
# 给你一个整数数组 nums ，判断是否存在三元组 [nums[i], nums[j], nums[k]] 满足 i != j、i != k 且 j != k ，同时还满足 nums[i] + nums[j] + nums[k] == 0 。请你返回所有和为 0 且不重复的三元组。
# 注意：答案中不可以包含重复的三元组。

# 输入：nums = [-1,0,1,2,-1,-4]
# 输出：[[-1,-1,2],[-1,0,1]]

# 输入：nums = [0,1,1]
# 输出：[]

# 输入：nums = [0,0,0]
# 输出：[[0,0,0]]

def s6(nums:list[int]) -> list[list[int]]:
    res = []
    if not nums or len(nums) < 3:
        return []
    nums.sort()
    for i in range(len(nums)):
        if nums[i] > 0:
            return res
        if nums[i] == nums[i+1]:
            continue
        l = i+1
        r = len(nums)-1
        while l<r:
            sum_lri = nums[i]+nums[l]+nums[r]
            if sum_lri < 0:
                l+=1
            if sum_lri > 0:
                r-=1
            if sum_lri == 0:
                res.append([nums[i],nums[l],nums[r]])
                while l<r and nums[l]==nums[l+1]:
                    l+=1
                while l<r and nums[r]==nums[r-1]:
                    r-=1
                l += 1
                r -= 1
    return res

def main():
    nums = list(map(int,input().strip().split()))
    res = s6(nums)
    print (res)

if __name__ == "__main__":
    main()