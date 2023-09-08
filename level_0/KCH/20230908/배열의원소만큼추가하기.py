# 예상 시간복잡도: O(N^2)
def solution(arr):
    res = []
    for i in arr:
        res.extend([i]*i)
    return res
