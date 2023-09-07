# 예상 시간복잡도: O(1)
def solution(a, b):
    answer = 0
    if a % 2 == 0 and b % 2 == 0 : #a and b are even
        if a < b:
            answer = b - a
        else:
            answer = a - b
    elif a % 2 != 0 and b % 2 != 0 : # a and b are odd
        answer = a * a + b * b

    else:
        answer = 2 * (a + b)
    return answer
