# 예상 시간 복잡도 O(n)
def solution(n):
    answer = 0
    while n > 0:
        answer = answer + 1
        if '3' in str(answer)  or answer % 3 == 0:
            pass
        else:
            n = n - 1
    return answer
