#예상 시간 복잡도 O(1)
def solution(arr):
    arr.remove(min(arr))
    if arr == []:
        arr.append(-1)
    return arr
