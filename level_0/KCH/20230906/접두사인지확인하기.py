# 예상 시간복잡도: O(K), K : 슬라이스 길이
def solution(my_string, is_prefix):
    return int(is_prefix == my_string[:len(is_prefix)])
