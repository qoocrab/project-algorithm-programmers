# 예상 시간 복잡도 O(n) n : N 자리수
def solution(n):
    answer = 0
    while n >= 10:
        answer = answer + (n % 10)
        n = n // 10
    answer = answer + n


    return answer
