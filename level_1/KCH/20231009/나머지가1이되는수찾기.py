# 예상 시간복잡도: O(N) 
def solution(n):
    for i in range(2,n+1): ## (n-1)//2+1
        if n%i == 1:
            return i
    # return n-1 ## O(N//2)
