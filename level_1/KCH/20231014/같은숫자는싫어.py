# 예상 시간복잡도: O(N)
def solution(arr):
    ex = arr[0]
    res = [ex]
    
    for i in range(1, len(arr)):
        if ex != arr[i]:
            res.append(arr[i])
            ex = arr[i]
    return res
