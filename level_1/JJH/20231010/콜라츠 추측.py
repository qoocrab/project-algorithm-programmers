# 예상 시간 복잡도 O(n)
def solution(num):
    answer = 0
    if num == 1:
        pass
    else:
        while num != 1:
            if num % 2 == 0:
                num = num // 2
            else:
                num = num *3 + 1
            answer = answer + 1
            if answer >= 500:
                answer = -1
                break
    return answer
