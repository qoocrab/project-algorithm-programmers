# 예상 시간복잡도: O(N)
def solution(s):
    res = s[0] if s[0].isdigit() else s[0].upper()
    for i in range(1,len(s)):
        if s[i] == ' ':
            res += s[i]
        elif s[i-1] == ' ' and not s[i].isdigit():
            res += s[i].upper()
        else:
            res += s[i].lower()
            
    return res
