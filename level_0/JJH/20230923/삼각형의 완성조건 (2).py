# 예상 시간 복잡도 O(sides[0] + sides[1])
def solution(sides):
    answer = 0
    for i in range(0, sides[0] + sides[1]):
        list = sides.copy()
        if max(list) > i:
            if i + min(list) > max(list):
                answer = answer + 1
            else:
                pass
        else:
            if sum(list) > i:
                answer = answer + 1

    return answer
