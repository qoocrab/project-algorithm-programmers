# 예상 시간복잡도: O(N)
def solution(myString, pat):
    res = 0
    for i in range(len(myString) - len(pat)+1):
        if myString[i] == pat[0] and myString[i:i+len(pat)] == pat:
            res += 1
    return res
