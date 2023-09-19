# 예상 시간 복잡도 O(n) n : letter length
def solution(n):
    answer = 0
    factorial = 1
    for i in range(1,11):
        factorial = factorial * i
        if factorial > n:
            answer = i - 1
            break
        elif factorial == n:
            answer = i
            break
    return answer
