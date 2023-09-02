# 예상 시간복잡도: O(n)
def solution(n):
    answer = 0
    if n % 2 == 0: # even number
        for i in range(0, n+1, 2):
            answer = answer + i * i
    else: # odd number
        for i in range(1, n+1, 2):
            answer = answer + i
    return answer
