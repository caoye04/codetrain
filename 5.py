# medium
# 5. 盛水最多的容器
# 给定一个长度为 n 的整数数组 height 。有 n 条垂线，第 i 条线的两个端点是 (i, 0) 和 (i, height[i]) 。
# 找出其中的两条线，使得它们与 x 轴共同构成的容器可以容纳最多的水。
# 返回容器可以储存的最大水量。
# 说明：你不能倾斜容器。

# 示例1:
# 输入：[1,8,6,2,5,4,8,3,7]
# 输出：49 
# 示例2:
# 输入：height = [1,1]
# 输出：1

def solution5(height):
    water = 0
    l = 0 
    r = len(height) - 1
    while l < r:
        if height[l] <= height[r]:
            water = max(water,height[l]*(r-l))
            l += 1
        else:
            water = max(water,height[r]*(r-l))
            r -= 1
    return water

def main():
    height = list(map(int,input().strip().split()))
    water = solution5(height)
    print (water)

if __name__ == "__main__":
    main()

