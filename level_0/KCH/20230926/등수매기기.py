# 예상 시간복잡도: O(N)
def solution(score):
    sorted_score = sorted([[sum(i)/2, idx] for idx, i in enumerate(score)], reverse=True) # [평균점수, 원배열에서의 idx]
    res = [0] * len(score)
    res[sorted_score[0][1]] = 1
    ck = 1
    
    for i in range(1, len(res)):
        if sorted_score[i-1][0] != sorted_score[i][0]: 
            ck = i+1
        res[sorted_score[i][1]] = ck
        
    return res
