# 예상 시간복잡도 : O(n) n : 입력 문자열
def solution(a, d, included):
    answer = 0

    for i in range(0, len(included)):
        if included[i]:
            answer = answer + (i) * d + a

    return answer
