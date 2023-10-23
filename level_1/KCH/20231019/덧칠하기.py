# 예상 시간복잡도: O(N)
def solution(n, m, section):
    n_start, cnt = section[0], 0
    
    for cur in section:
        if cur < n_start:
            continue
        cnt += 1
        n_start = cur+m
        
    return cnt
