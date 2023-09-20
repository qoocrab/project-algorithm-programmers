# 예상 시간복잡도: O(N)
def solution(array, n):
    res = -9999
    for num in array:
        if abs(n - num) <= abs(n - res):
            if abs(n - num) == abs(n - res) and num > res :
                continue
            res = num
    return res
