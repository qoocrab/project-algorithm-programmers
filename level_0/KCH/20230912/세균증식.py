# 예상 시간복잡도: O(1)
def solution(n, t):
    return n*(2**t)

### cf)
def solution(n, t):
    return n << t
