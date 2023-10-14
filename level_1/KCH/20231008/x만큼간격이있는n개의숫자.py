# 예상 시간복잡도: O(N)
def solution(x, n):
    if x == 0:
        return [x]*n
    return list(range(x, (n+1)*x, x))
