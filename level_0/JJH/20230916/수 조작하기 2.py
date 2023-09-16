# 예상 시간복잡도: O(n) n : numLog length
def solution(numLog):
    answer = []
    init = 0
    for i in range(0,len(numLog)):
        if i == 0:
            continue
        else:
            if numLog[i] - numLog[i-1] == 1:
                answer.append('w')
            elif numLog[i] - numLog[i-1] == -1:
                answer.append('s')
            elif numLog[i] - numLog[i-1] == 10:
                answer.append('d')
            elif numLog[i] - numLog[i-1] == -10:
                answer.append('a')

    return ''.join(answer)
