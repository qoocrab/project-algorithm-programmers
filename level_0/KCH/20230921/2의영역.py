# 예상 시간복잡도: O(N)
def solution(arr):
    l_idx, r_idx = None, None
    for i in range(len(arr)):
        if arr[i] == 2:
            if not l_idx:
                l_idx = i
            r_idx = i
        
    if l_idx and r_idx:
        return arr[l_idx:r_idx+1]
    return [-1]
