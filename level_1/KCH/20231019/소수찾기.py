# 예상 시간복잡도: O(NlogN)
def solution(n):
    tmp = [True for _ in range(n+1)]
    for i in range(2, n):
        if tmp[i]:
            for j in range(2*i, n+1, i):
                tmp[j] = False
    tmp[1] = True
    
    return sum(tmp[2:])
