# 예상 시간복잡도: O(N)
def solution(arr, queries):
    for i,j in queries:
        arr[i], arr[j] = arr[j], arr[i]
    return arr
