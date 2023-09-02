# 예상 시간복잡도: O(1)
def solution(n, k):
    answer = 0
    answer = answer + n * 12000
    k = k - int(n//10)
    if 0 < k:
        answer = answer + k * 2000
    return answer
