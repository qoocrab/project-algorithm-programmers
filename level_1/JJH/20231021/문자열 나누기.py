def solution(s):
    answer = 0

    String = s
    while len(String) > 0:
        xNum = 0
        notXNum = 0
        for i in range(0,len(String)):
            done = True
            if String[0] == String[i]:
                xNum += 1
            else:
                notXNum += 1
            if xNum == notXNum:
                answer += 1
                String = String[i+1:]
                done = False
                break
        if done:
            answer += 1
            break
    return answer

print(solution("abracadabra"))