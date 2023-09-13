# 예상 시간복잡도: O(1)
def solution(my_string, k):
    list = []
    for i in range(0,k):
        list.append(my_string)
    return ''.join(list)
