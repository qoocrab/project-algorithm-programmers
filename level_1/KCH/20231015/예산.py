# 예상 시간복잡도: O(N)
def solution(d, budget):
    d.sort()
    for i in range(len(d)):
        budget -= d[i]
        if budget < 0 : 
            return i
    else: 
        return i+1
