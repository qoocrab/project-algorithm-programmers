# 예상 시간복잡도: O(N)
def solution(k, m, score):
    score.sort()
    score = score[len(score)%m:][::m]
    res = sum(score)*m
        
    return res
