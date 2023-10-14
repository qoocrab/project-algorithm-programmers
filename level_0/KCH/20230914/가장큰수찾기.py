# 예상 시간복잡도: O(N)
def solution(array):
    IDX = 0
    for i in range(len(array)):
        if array[IDX] < array[i]:
            IDX = i
    return [array[IDX], IDX]
