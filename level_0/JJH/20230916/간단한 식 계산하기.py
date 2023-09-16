# 예상 시간복잡도: O(1)
def solution(binomial):
    answer = 0
    input = binomial.split(' ')
    if input[1] == '+':
        answer = int(input[0]) + int(input[2])
    elif input[1] == '-':
        answer = int(input[0]) - int(input[2])
    elif input[1] == '*':
        answer = int(input[0]) * int(input[2])
    return answer
