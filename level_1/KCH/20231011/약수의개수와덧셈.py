# 예상 시간복잡도: O(N)
def solution(left, right):
    res = 0
    for i in range(left, right+1):
        if (i**0.5)%1 == 0:
            res -= i
        else: res += i
    return res
