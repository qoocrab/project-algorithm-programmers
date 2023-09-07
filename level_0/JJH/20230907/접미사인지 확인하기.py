# 예상 시간복잡도: O(1)
def solution(my_string, is_suffix):
    answer = 0
    if my_string.find(is_suffix) == len(my_string) - len(is_suffix):
        answer = 1
    else:
        answer = 0
    return answer
