# 예상 시간복잡도: O(K), K:is_suffix 길이
def solution(my_string, is_suffix):
    return int(my_string[-len(is_suffix):] == is_suffix)
