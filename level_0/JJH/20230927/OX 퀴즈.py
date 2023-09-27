# 예상 시간 복잡도 O(n) n quiz length
def solution(quiz):
    answer = []
    for i in quiz:
        equation = i.split()
        if int(equation[-1]) == mathSolver(equation[0] + ' ' + equation[1] + ' ' + equation[2]):
            answer.append('O')
        else:
            answer.append('X')
    return answer

def mathSolver(stringEquation):
    equationList = stringEquation.split()
    if equationList[1] == '-':
        result = int(equationList[0]) - int(equationList[2])
    else:
        result = int(equationList[0]) + int(equationList[2])
    return result
