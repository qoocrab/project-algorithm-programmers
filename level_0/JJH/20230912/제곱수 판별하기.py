# 예상 시간복잡도: O(1)
def solution(n):
    answer = 0
    tmp = n ** (1 / 2)
    intTmp = int(tmp)
    if tmp == intTmp:
        answer = 1
    else:
        answer = 2
    return answer

