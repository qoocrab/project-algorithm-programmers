# 예상 시간 복잡도 O(n) n : l - r
def solution(l, r):
    answer = []
    for i in range(l,r+1):
        string = str(i)
        if '1' in string or '2' in string or '3' in string or '4' in string or '6' in string or '7' in string or '8' in string or '9' in string:
            pass
        else:
            answer.append(i)
    if answer == []:
        answer.append(-1)
    return answer
