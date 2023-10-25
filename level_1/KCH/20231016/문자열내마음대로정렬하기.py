# 예상 시간복잡도: O(N)
def solution(strings, n):
    return sorted(strings, key = lambda x: (x[n], x))
