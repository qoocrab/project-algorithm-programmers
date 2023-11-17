# 예상 시간복잡도: O(N)
def solution(citations):
    citations.sort()
    res = 0
    
    for i in range(len(citations)):
        if len(citations) - i<=citations[i]:
            res = len(citations) - i
            break
            
    return res
