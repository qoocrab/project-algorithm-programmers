# 예상 시간복잡도: O(N)
def solution(brown, yellow):
    res = []
    for yw in range(1, yellow+1): 
        yh = yellow/yw
        if yh%1!=0 and yw*yh!=yellow:
            continue
        
        if (yw+yh+4)*2-4 == brown:
            res = [yw+2, yh+2]
            return sorted(res, reverse=True)
