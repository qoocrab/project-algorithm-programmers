# 예상 시간 복잡도 O(n) n numbers length
def solution(numbers):
    answer = []
    char = []
    for i in numbers:
        char.append(i)
        if ''.join(char) == 'zero':
            answer.append('0')
            char = []
        elif ''.join(char) == 'one':
            answer.append('1')
            char = []
        elif ''.join(char) == 'two':
            answer.append('2')
            char = []
        elif ''.join(char) == 'three':
            answer.append('3')
            char = []
        elif ''.join(char) == 'four':
            answer.append('4')
            char = []
        elif ''.join(char) == 'five':
            answer.append('5')
            char = []
        elif ''.join(char) == 'six':
            answer.append('6')
            char = []
        elif ''.join(char) == 'seven':
            answer.append('7')
            char = []
        elif ''.join(char) == 'eight':
            answer.append('8')
            char = []
        elif ''.join(char) == 'nine':
            answer.append('9')
            char = []
        else:
            pass
    return int(''.join(answer))
