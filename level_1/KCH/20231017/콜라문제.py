# 예상 시간복잡도: O(logN)
def solution(a, b, n):
    res = 0
    while n//a>0:
        tmp = (n//a)*b
        n %= a
        n += tmp
        res += tmp
    return res
