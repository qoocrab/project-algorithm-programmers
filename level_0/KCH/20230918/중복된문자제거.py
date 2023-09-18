# 예상 시간복잡도: O(N)
def solution(my_string):
    return ''.join(dict.fromkeys(my_string))
