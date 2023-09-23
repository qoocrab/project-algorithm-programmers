# 예상 시간복잡도: O(N)
def solution(arr, k):
    visited = [0] * 100000
    res = []
    for i in range(len(arr)):
        if len(res) == k:
            return res
        if not visited[arr[i]]:
            visited[arr[i]] = 1
            res.append(arr[i])
            
    return res + [-1]*(k-len(res))
