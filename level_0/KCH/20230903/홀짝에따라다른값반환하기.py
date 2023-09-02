# 예상 시간복잡도: O(N)
def solution(n):
    ans = 0
    for i in range(n%2,n+1,2):
        ans += i**((n+1)%2 + 1)
        
    return ans
