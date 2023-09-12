# 예상 시간복잡도: O(N)
def solution(arr, n):
    for i in range((int(len(arr)%2)+1)%2,len(arr),2):
        arr[i] += n
    return arr
