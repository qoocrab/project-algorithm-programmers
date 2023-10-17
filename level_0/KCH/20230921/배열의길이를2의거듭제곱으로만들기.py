# 예상 시간복잡도: O(logN)
def solution(arr):
    leng = len(arr)
    cnt = 0
    while leng>1:
        leng /=2
        cnt += 1
    return arr + [0]*(2**cnt - len(arr))
