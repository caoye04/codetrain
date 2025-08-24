# medium
# 8.找到字符串中所有字母异位词
# 给定两个字符串 s 和 p，找到 s 中所有 p 的 异位词 的子串，返回这些子串的起始索引。不考虑答案输出的顺序。
# 输入: s = "cbaebabacd", p = "abc"
# 输出: [0,6]
# 输入: s = "abab", p = "ab"
# 输出: [0,1,2]

def s8(s,p):
    res = []
    len_s = len(s)
    len_p = len(p)
    cnt_p = [0] * 26
    cnt_s = [0] * 26
    if len_s < len_p:
        return []
    for i in range(len_p):
        cnt_s[ord(s[i])-ord("a")] += 1
        cnt_p[ord(p[i])-ord("a")] += 1
    if cnt_p == cnt_s:
        res.append(0)
    for i in range(len_p,len_s):
        cnt_s[ord(s[i]) - ord("a")] += 1
        cnt_s[ord(s[i-len_p]) - ord("a")] -= 1
        if cnt_s == cnt_p:
            res.append(i - len_p + 1)
    return res

def main():
    s = input().strip()
    p = input().strip()
    res = s8(s,p)
    print(res)

if __name__ == "__main__":
    main()


