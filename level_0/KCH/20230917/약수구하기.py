# 예상 시간복잡도: O(N)
def solution(n):
    return [i for i in range(1, n+1) if n%i==0]
