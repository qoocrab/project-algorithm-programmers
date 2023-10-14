# 예상 시간복잡도: O(N)
def solution(x):
    SUM = sum(map(int,list((str(x)))))
    return x%SUM == 0.0
