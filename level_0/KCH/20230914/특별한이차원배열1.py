# 예상 시간복잡도: O(N*N)
def solution(n):
    return [[1 if i==j else 0 for i in range(n)]for j in range(n)]
