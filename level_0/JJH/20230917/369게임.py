# 예상 시간복잡도 : O(n) n : order length
def solution(order):
    answer = 0
    while order // 10 > 0:
        remain = order % 10
        if remain == 3 or remain == 6 or remain == 9:
            answer = answer + 1
        order = order // 10
    if order % 10 == 3 or order % 10 == 6 or order % 10 == 9:
        answer = answer + 1
    return answer
