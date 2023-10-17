# 예상 시간복잡도: O(N*N)
def solution(arr):
    n = len(arr)
    for i in range(n//2+1):
        for j in range(n//2+1):
            if arr[i][j] != arr[j][i]:
                return 0
    return 1

# cf) 쩐당
def solution(arr):
    return int(arr == list(map(list, zip(*arr))))
