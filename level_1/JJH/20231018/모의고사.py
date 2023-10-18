def solution(answers):
    aSolution = [1, 2, 3, 4, 5]
    bSolution = [2, 1, 2, 3, 2, 4, 2, 5]
    cSolution = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    answer = []
    aScore = getGrade(aSolution, answers)
    bScore = getGrade(bSolution, answers)
    cScore = getGrade(cSolution, answers)
    scoreList = [aScore, bScore, cScore]
    maxScore = max(scoreList)
    if aScore == maxScore:
        answer.append(1)

    if bScore == maxScore:
        answer.append(2)

    if cScore == maxScore:
        answer.append(3)
    return answer


def getGrade(solution, answers):
    score = 0
    for i in range(0, len(answers)):
        if answers[i] == solution[i % len(solution)]:
            score = score + 1
    return score

    return answer
