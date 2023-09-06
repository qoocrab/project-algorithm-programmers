# 예상 시간복잡도: O(n)
def solution(my_string, is_prefix):
    answer = 0
    if my_string.find(is_prefix) == 0:
        answer = 1
    else:
        answer = 0
    return answer
