# 예상 시간복잡도: O(N)
def solution(str1, str2):
    res = ''
    for a, b in zip(str1, str2):
        res += a
        res += b
    return res
