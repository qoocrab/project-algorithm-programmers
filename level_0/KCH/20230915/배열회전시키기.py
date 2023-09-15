# 예상 시간복잡도: O(N)
def solution(numbers, direction):
    option = {'right' : -1, 'left':1}
    return numbers[option[direction]:] + numbers[:option[direction]]
