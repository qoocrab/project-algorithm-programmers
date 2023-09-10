# 예상 시간복잡도: O(1)
def solution(array):
    array.sort()
    if len(array) % 2 == 0:
        index = (len(array) // 2) - 1
    else:
        index = (len(array) // 2)
    return array[index]

