# medium
# 3. 最长连续序列
# 给定一个未排序的整数数组 nums ，找出数字连续的最长序列（不要求序列元素在原数组中连续）的长度。请你设计并实现时间复杂度为 O(n) 的算法解决此问题。
# 示例 1：
# 输入：nums = [100,4,200,1,3,2]
# 输出：4
# 示例 2：
# 输入：nums = [0,3,7,2,5,8,4,6,0,1]
# 输出：9
# 示例 3：
# 输入：nums = [1,0,1,2]
# 输出：3
# 提示：
# 0 <= nums.length <= 105
# -109 <= nums[i] <= 109

def solution3(nums):
    ans = 0
    set_num = set(nums)
    for x in set_num:
        if x-1 in set_num:
            continue
        y = x + 1
        while y in set_num:
            y += 1
        ans = max(ans,y-x)
    return ans
def main(): 
    nums_input = input().strip().split()
    nums = list(map(int,nums_input))
    result = solution3(nums)
    print(result)
if __name__ == "__main__":
    main()