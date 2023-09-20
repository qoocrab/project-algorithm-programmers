# 예상 시간복잡도: O(1)
def solution(arr, intervals):
    [a1, a2], [b1, b2] = intervals
    return arr[a1:a2+1] + arr[b1:b2+1]
