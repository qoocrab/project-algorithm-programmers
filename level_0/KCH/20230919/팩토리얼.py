# 예상 시간복잡도: O(N)
def solution(n):
    fac, cnt = 1, 1
    while fac <= n:
        fac *= cnt
        cnt += 1
    
    return cnt-2
