# 4. 移动零
# 给定一个数组 nums，编写一个函数将所有 0 移动到数组的末尾，同时保持非零元素的相对顺序。请注意 ，必须在不复制数组的情况下原地对数组进行操作。

# 示例 1:
# 输入: nums = [0,1,0,3,12]
# 输出: [1,3,12,0,0]
# 示例 2:
# 输入: nums = [0]
# 输出: [0]

# 进阶：你能尽量减少完成的操作次数吗？

def solution4(nums):
    l = 0
    for r in range(len(nums)):
        if nums[r] == 0:
            continue
        nums[l],nums[r]=nums[r],nums[l]
        l += 1

def main():
    nums = list(map(int,input().strip().split()))
    solution4(nums)
    print(nums)

if __name__ == "__main__":
    main()