# 예상 시간복잡도: O(N)
def solution(n):
    dp = [0 for _ in range(n)]
    dp[0] = 1
    if n>1: dp[1] = 2

    for i in range(2,n):
        dp[i] = (dp[i-1] + dp[i-2])%1234567
        
    return dp[-1]

# 피보나치 가능
# def solution(n):
#     a, b = 1, 2
#     for i in range(2,n):
#         a, b = b, a+b
#     return b
