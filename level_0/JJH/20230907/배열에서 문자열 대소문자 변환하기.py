# 예상 시간복잡도: O(n)
def solution(strArr):
    answer = []
    count = 0
    for i in strArr:
        if count % 2 == 0:
            answer.append(i.lower())
        else:
            answer.append(i.upper())
        count = count + 1
    return answer
