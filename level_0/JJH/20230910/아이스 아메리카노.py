# 예상 시간복잡도: O(1)
def solution(money):
    answer = []
    answer.append(money // 5500)
    answer.append(money % 5500)
    return answer
