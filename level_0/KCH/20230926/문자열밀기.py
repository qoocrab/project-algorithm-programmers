# 예상 시간복잡도: O(N)
def solution(A, B):
    for i in range(len(A)):
        if A[-i:] + A[:-i] == B:       
            return i
    return -1

# cf) lambda a,b:(b*2).find(a)
