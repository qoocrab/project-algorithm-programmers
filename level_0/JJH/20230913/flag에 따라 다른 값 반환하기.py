# 예상 시간복잡도: O(1)
def solution(a, b, flag):
    answer = 0
    if flag:
        answer = a + b
    else:
        answer = a - b
    return answer
