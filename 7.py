# medium
#  7. 无重复字符的最长子串
# 给定一个字符串 s ，请你找出其中不含有重复字符的 最长子串的长度。
# 输入: s = "abcabcbb"
# 输出: 3 
# 输入: s = "bbbbb"
# 输出: 1
# 输入: s = "pwwkew"
# 输出: 3

def s7(s):
    res = 0
    hash_map = {}
    l = 0
    for r in range(len(s)):
        hash_map[s[r]] = hash_map.get(s[r],0) + 1
        if(len(hash_map)==r-l+1):
            res = max(res,r-l+1)
        while r-l+1>len(hash_map):
            head = s[l]
            hash_map[head] -= 1
            if hash_map[head] == 0:
                del hash_map[head]
            l+=1
    return res

def main():
    s = input().strip()
    res = s7(s)
    print (res)

if __name__ == "__main__":
    main()

