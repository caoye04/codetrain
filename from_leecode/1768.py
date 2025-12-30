# 1768.交替合并字符串
# 给你两个字符串 word1 和 word2 。请你从 word1 开始，通过交替添加字母来合并字符串。如果一个字符串比另一个字符串长，就将多出来的字母追加到合并后字符串的末尾。
# 返回 合并后的字符串 。

# 点评：version1方法暴力粗糙,消耗内存过高
def solution_1768_version1(word1,word2):
    len1 = len(word1)
    len2 = len(word2)
    result = ""
    if len1 == len2 :
        for i in range(len1):
            result += word1[i]
            result += word2[i]
    if len1 < len2 :
        for i in range(len1):
            result += word1[i]
            result += word2[i]
        for i in range(len2-len1):
            result += word2[len1+i]
    if len1 > len2 :
        for i in range(len2):
            result += word1[i]
            result += word2[i]
        for i in range(len1-len2):
            result += word1[len2+i]
    return result

# 点评：version2方法整体简洁优雅了不少，但是似乎还是内存占用过高
def solution_1768_version2(word1,word2):
    len1 = len(word1)
    len2 = len(word2)
    i , j = 0, 0 
    ans = ""
    while i < len1 or j < len2 :
        if i < len1:
            ans += word1[i]
            i += 1
        if j < len2:
            ans += word2[j]
            j += 1
    return ans

# 点评：version3虽然和2几乎一样，但是内存占比低了很多，可以看得出来list类的处理对资源需求更低
def solution_1768_version3(word1,word2):
    result_list = []
    i , j = 0 , 0
    while i<len(word1) or j<len(word2):
        if i<len(word1):
            result_list.append(word1[i])
            i+=1
        if j<len(word2):
            result_list.append(word2[j])
            j+=1
    return "".join(result_list)

word2 = "abc"
word1 = "eeeeeeee"
res = solution_1768_version3(word1,word2)
print(res)