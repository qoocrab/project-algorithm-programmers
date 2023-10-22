# 예상 시간 복잡도

def solution(N, stages):
    answer = []
    stageList = [0 for i in range(0, len(stages))]
    for i in range(0, len(stages)):
        stageList[stages[i]-1] += 1

    for m in range(0, N):
        answer.append(sum(stageList[m:]))

    result = []
    for k in range(0,len(answer)):
        min = 501
        for l in range(k,len(answer)):
            if k < min:
                min = k


    return answer

print(solution(5,[2,1,2,6,2,4,3,3]))