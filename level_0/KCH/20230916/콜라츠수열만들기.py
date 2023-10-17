# 예상 시간복잡도: O(1)
def solution(n):
    res = [n]
    while n!=1:
        if n%2:
            n = 3*n + 1
        else: n//=2
        res.append(n)
    return res
