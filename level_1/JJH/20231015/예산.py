# 예상 시간 복잡도 O(n)
def solution(d, budget):
    answer = 0
    d.sort()
    for i in d:
        if budget - i < 0:
            break
        else:
            budget = budget - i
            answer = answer + 1

    return answer
