# 예상 시간복잡도: O(N)
def solution(arr):
    arr.remove(min(arr))
    return arr if arr else [-1]
