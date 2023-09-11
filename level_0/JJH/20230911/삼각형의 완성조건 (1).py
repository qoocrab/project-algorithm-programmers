# 예상 시간복잡도: O(1)
def solution(sides):
    answer = 0
    sides.sort()
    if sides[2] < sides[0] + sides[1]:
        answer = 1
    else:
        answer = 2
    return answer
