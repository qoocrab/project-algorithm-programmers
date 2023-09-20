# 예상 시간복잡도: O(1)
def solution(a, b, c):
    S = set([a,b,c])
    SUM = 1
    for i in range(1,5-len(S)):
        SUM *= (a**i + b**i + c**i)
    return SUM
