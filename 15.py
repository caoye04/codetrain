# medium
# 15. 螺旋矩阵
# 给你一个 m 行 n 列的矩阵 matrix ，请按照 顺时针螺旋顺序 ，返回矩阵中的所有元素。
# 输入：matrix = [[1,2,3],[4,5,6],[7,8,9]]
# 输出：[1,2,3,6,9,8,7,4,5]
# 输入：matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
# 输出：[1,2,3,4,8,12,11,10,9,5,6,7]

def spiralOrder(matrix):
        left = 0
        right = len(matrix[0])-1
        up = 0
        down = len(matrix)-1
        sumnum = (down+1) * (right+1)
        # print(sumnum)
        direction = 1
        res = []
        while len(res) < sumnum:
            if direction == 1:
                for i in range(left, right + 1):
                    res.append(matrix[up][i])
                up += 1
                direction = 2
            elif direction == 2:
                for i in range(up, down + 1):
                    res.append(matrix[i][right])
                right -= 1
                direction = 3
            elif direction == 3:
                for i in range(right, left - 1, -1):
                    res.append(matrix[down][i])
                down -= 1
                direction = 4
            elif direction == 4:
                for i in range(down, up - 1, -1):
                    res.append(matrix[i][left])
                left += 1
                direction = 1
        return res

def main():
    matrix = list(list())
    m = int(input())
    for i in range(m):
        nums = list(map(int,input().strip().split()))
        matrix.append(nums)
    res=spiralOrder(matrix)
    print (res)

if __name__ =="__main__":
    main()