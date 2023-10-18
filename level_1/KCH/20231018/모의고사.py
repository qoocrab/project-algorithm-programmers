# 예상 시간복잡도: O(N)
def solution(answers):
    p1 = [1,2,3,4,5,1,2,3,4,5]
    p2 = [2,1,2,3,2,4,2,5]
    p3 = [3,3,1,1,2,2,4,4,5,5]
    res = [0, 0, 0]
    for i in range(len(answers)):
        if answers[i] == p1[i%10] : res[0] += 1
        if answers[i] == p2[i%8] : res[1] += 1
        if answers[i] == p3[i%10] : res[2] += 1
    
    tmp = []
    for i in range(len(res)):
        if res[i] == max(res):
            tmp.append(i+1)
    return tmp
