# 예상 시간복잡도: O(N**2)
def solution(n):
    res = 0
    for i in range(n+1):
        for j in range(2,i):
            if i%j == 0 :
                res += 1
                break
    return res
