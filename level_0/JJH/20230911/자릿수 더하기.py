# 예상 시간복잡도: O(n)
def solution(n):
    answer = 0
    while n // 10 > 0:
        answer = answer + (n % 10)
        n = n // 10
    answer = answer + n
    return answer
