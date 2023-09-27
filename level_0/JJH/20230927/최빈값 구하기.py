# 예상 시간 복잡도 O(n) n array max value
def solution(array):
    answer = 0
    appear_list = [0 for i in range(0, max(array) + 1)]
    for i in array:
        appear_list[i] = appear_list[i] + 1

    maxAppearedCount = 0
    maxAppearedIndex = -1
    for i in range(0, len(appear_list)):
        if maxAppearedCount < appear_list[i]:
            maxAppearedCount = appear_list[i]
            maxAppearedIndex = i
    if appear_list.count(maxAppearedCount) > 1:
        return -1
    return maxAppearedIndex
