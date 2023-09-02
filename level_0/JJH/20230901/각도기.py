# 예상 시간복잡도: O(1)
def solution(angle):
    answer = 0
    if 0 < angle and angle < 90:
        answer = 1
    elif angle is 90:
        answer = 2
    elif 90 < angle and angle < 180:
        answer = 3
    elif angle is 180:
        answer = 4
    else:
        answer = -1
    return answer
