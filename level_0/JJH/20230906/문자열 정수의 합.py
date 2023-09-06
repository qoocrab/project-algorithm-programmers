# 예상 시간복잡도: O(n)
def solution(num_str):
    answer = 0
    num = int(num_str)
    while num // 10 != 0:
        answer = answer + num % 10
        num = num // 10
    answer = answer + num
    return answer

