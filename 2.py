# medium
# 2.字母异位词分组
# 给你一个字符串数组，请你将 字母异位词 组合在一起。可以按任意顺序返回结果列表。
# 示例 1:
# 输入: strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
# 输出: [["bat"],["nat","tan"],["ate","eat","tea"]]
# 示例 2:
# 输入: strs = [""]
# 输出: [[""]]
# 示例 3:
# 输入: strs = ["a"]
# 输出: [["a"]]
# 提示：
# 1 <= strs.length <= 104
# 0 <= strs[i].length <= 100
# strs[i] 仅包含小写字母

def solution2(strs:list[str])->list[list[str]]:
    alphanum = [2,3,5,7,11,
                13,17,19,23,29,
                31,37,41,43,47,
                53,59,61,67,71,
                73,79,83,89,97,
                101]
    result = dict()
    for str in strs:
        prod = 1
        for item in str:
            prod = alphanum[ord(item)-ord('a')]*prod
        if prod not in result:
            result[prod] = []
        result[prod].append(str)
    return list(result.values())

def main():
    strs = input().strip().split()
    result = solution2(strs)
    print(result)

if __name__ == "__main__":
    main()


        

    
