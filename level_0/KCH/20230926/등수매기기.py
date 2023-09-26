# 예상 시간복잡도: O(N)
def solution(score):
    tmp = []
    for idx, i in enumerate(score):
        tmp.append([sum(i)/2,idx])
    
    tmp = sorted(tmp, reverse=True)
    res = [0] * len(score)
    res[tmp[0][1]] = 1
    ck = 1
    
    for i in range(1, len(res)):
        if tmp[i-1][0] != tmp[i][0]: 
            ck = i+1
        res[tmp[i][1]] = ck
        
    return res
