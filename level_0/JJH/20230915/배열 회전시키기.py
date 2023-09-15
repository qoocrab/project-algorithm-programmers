# 예상 시간복잡도: O(n) n : numbers length
def solution(numbers, direction):
    answer = []
    if direction == 'right':
        answer = numbers[0:len(numbers)-1]
        answer.insert(0,numbers[len(numbers)-1])
    else:
        answer = numbers[1:]
        answer.append(numbers[0])
    return answer
