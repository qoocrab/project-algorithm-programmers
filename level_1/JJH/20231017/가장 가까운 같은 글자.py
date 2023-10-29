# 예상 시간 복잡도 O(n^2)
def solution(s):
    answer = []

    for k in range(0, len(s)):
        found = False
        for i in range(k-1,-1,-1):
            if (s[k] == s[i]):
                answer.append(k-i)
                found = True
                break
            else:
                pass
        if found:
            pass
        else:
            answer.append(-1)
    return answer
