# 예상 시간복잡도: O(N)
def solution(n, lost, reserve):
    cnt = 0
    R = list(set(reserve) - set(lost))
    L = list(set(lost) - set(reserve))
    
    for i in range(len(L)):        
        if L[i]-1 in R:
            R.remove(L[i]-1)
            cnt += 1
        
        elif L[i]+1 in R:
            R.remove(L[i]+1)
            cnt += 1
            
    return n - len(L) + cnt
