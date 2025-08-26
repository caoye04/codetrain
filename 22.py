# medium
# 22.括号生成
# 数字 n 代表生成括号的对数，请你设计一个函数，用于能够生成所有可能的并且 有效的 括号组合。
# 输入：n = 3
# 输出：["((()))","(()())","(())()","()(())","()()()"]
# 输入：n = 1
# 输出：["()"]

n = int(input())
ans = []
def solu(S,l,r):
    if len(S)==2*n:
        ans.append("".join(S))
        return
    if l<n:
        S.append('(')
        solu(S,l+1,r)
        S.pop()
    if r<l:
        S.append(')')
        solu(S,l,r+1)
        S.pop()
solu([],0,0)
print(ans)
print(len(ans))