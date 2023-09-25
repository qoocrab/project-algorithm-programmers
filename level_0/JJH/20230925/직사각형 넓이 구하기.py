# 예상 시간 복잡도 O(1)
def solution(dots):
    answer = 0
    for i in range(0,4):
        if dots[0][0] != dots[i][0]:
            width = abs(dots[0][0] - dots[i][0])
        if dots[0][1] != dots[i][1]:
            height = abs(dots[0][1] - dots[i][1])
    answer = width * height
    return answer
