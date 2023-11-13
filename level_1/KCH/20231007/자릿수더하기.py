# 예상 시간복잡도: O(N)
def solution(n):
    op = lambda x: int(x)
    return sum([op(i) for i in str(n)])
