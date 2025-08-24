# medium
# 9. 和为K的子数组
# 给你一个整数数组 nums 和一个整数 k ，请你统计并返回 该数组中和为 k 的子数组的个数 。
# 子数组是数组中元素的连续非空序列。
# 输入：nums = [1,1,1], k = 2
# 输出：2
# 输入：nums = [1,2,3], k = 3
# 输出：2

# 思路：算出每一个点的presum，做差找k

def s9(nums,k):
    ans = 0
    len_num = len(nums)
    pre_sum = [0]*(len_num+1)
    pre_sum[0] = 0
    for i in range(1,len_num+1):
        pre_sum[i] = pre_sum[i-1]+nums[i-1]
    for l in range(len_num+1):
        r = l+1
        while r < len_num+1:
            if pre_sum[r]-pre_sum[l] == k:
                ans += 1
                r += 1
            elif pre_sum[r]-pre_sum[l] < k:
                r += 1
            elif pre_sum[r]-pre_sum[l] > k:
                break
    return ans

nums = list(map(int,input().strip().split()))
k = int(input())
ans=s9(nums,k)
print(ans)


        

