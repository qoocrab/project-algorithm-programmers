# 예상 시간 복잡도 : O(s)
def solution(s):
    answer = []
    for i in range(0, len(s)):

        if s[i] in ''.join([s[0:i], s[i + 1:]]):
            pass
        else:
            answer.append(s[i])
    answer.sort()
    return ''.join(answer)
