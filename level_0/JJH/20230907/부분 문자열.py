# 예상 시간복잡도: O(n)
def solution(str1, str2):
    answer = 0
    if str2.find(str1) >= 0:
        answer = 1
    else:
        answer = 0
    return answer
