# 예상 시간복잡도: O(1)
def solution(str1, str2):
    answer = 0
    if str1.find(str2) >= 0:
        answer = 1
    else:
        answer = 2
    return answer
