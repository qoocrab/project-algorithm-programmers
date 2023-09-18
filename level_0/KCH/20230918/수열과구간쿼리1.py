# 예상 시간복잡도: O(N**2)
def solution(arr, queries):
    for s,e in queries:
        arr[s:e+1] = [i+j for i,j in zip(arr[s:e+1], [1] * (e-s+1))]
    return arr
