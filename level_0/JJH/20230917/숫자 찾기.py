# 예상 시간복잡도 : O(n) n : num length
def solution(num, k):
    if str(k) in str(num):
        answer = str(num).index(str(k)) + 1
    else:
        answer = -1
    return answer
