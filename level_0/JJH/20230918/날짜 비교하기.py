# 예상 시간 복잡도 : O(1)
def solution(date1, date2):
    answer = 0
    for i in range(0, len(date1)):
        answer = compare(date1[i], date2[i])
        if answer >= 0:
            break
    if answer == -1:
        answer = 0
    return answer


def compare(a, b):
    if a > b:
        return 0
    elif a < b:
        return 1
    else:
        return -1
