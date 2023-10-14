# 예상 시간복잡도: O(N)
def solution(arr):
    leng = max(len(arr), len(arr[0]))
    if leng == len(arr): # arr : 가로가 큰 직사각형
        for i in range(len(arr)):
            arr[i] += [0] * (leng - len(arr[i]))
    else:
        arr.extend([[0] * (len(arr[0]))] * (leng - len(arr)))
        
    return arr
