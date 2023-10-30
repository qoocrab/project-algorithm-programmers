def solution(dartResult):
    answer = 0
    prevScore = 0
    score = 0
    for i in range(0, len(dartResult)):
        if dartResult[i].isdigit():
            if dartResult[i-1] == "1" and dartResult[i] == "0":
                score = 10

            else:
                prevScore = score
                score = int(dartResult[i])
        elif dartResult[i].isalpha():

            if dartResult[i] == 'S':
                pass
            elif dartResult[i] == 'D':
                score = score ** 2
            elif dartResult[i] == 'T':
                score = score ** 3


            answer = answer + score
        elif dartResult[i] == "*":
            answer = answer - score - prevScore
            score = prevScore*2 + score * 2
            answer = answer + score
            prevScore = score
        elif dartResult[i] == "#":
            answer = answer - score
            score = -1 * score
            answer = answer + score
            prevScore = score
    return answer

print(solution("10S1S0S*"))