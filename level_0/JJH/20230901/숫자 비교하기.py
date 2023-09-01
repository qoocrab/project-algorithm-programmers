# 예상 시간복잡도: O(1)
def solution(num1, num2):
    result = 0
    if(num1 == num2):
        result = 1
    else:
        result = -1
    return result