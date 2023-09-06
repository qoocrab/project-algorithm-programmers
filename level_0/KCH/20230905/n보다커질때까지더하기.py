# 예상 시간복잡도: O(N)
def solution(numbers, n):
    ans = 0
    for i in numbers:
        ans += i
        if ans > n:
            return ans
    return 
