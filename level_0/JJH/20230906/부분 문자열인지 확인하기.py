# 예상 시간복잡도: O(n)
def solution(my_string, target):
    answer = 0
    if 0 <= my_string.find(target):
        answer = 1
    else:
        answer = 0
    return answer
