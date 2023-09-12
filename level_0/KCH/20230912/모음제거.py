# 예상 시간복잡도: O(N)
def solution(my_string):
    return ''.join([i for i in my_string if i not in {'a', 'e', 'i', 'o', 'u'}])
