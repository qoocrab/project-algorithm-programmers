# 예상 시간 복잡도 O(1)
def solution(s):
    answer = []
    if len(s) % 2 == 0:
        answer.append(s[len(s)//2 - 1])
        answer.append(s[len(s)//2])
    else:
        answer.append(s[len(s)//2])
    return ''.join(answer)
