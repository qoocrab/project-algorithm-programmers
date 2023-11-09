# 예상 시간복잡도: O(N)
def solution(A,B):
    res = 0
    A.sort()
    B.sort()
    for i in range(len(A)):
        res += A[i]*B[-i-1]
        
    return res
