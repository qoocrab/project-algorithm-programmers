# 예상 시간복잡도: O(n)
def solution(array, n):
    answer = 0
    for i in array:
        if i == n:
            answer = answer + 1
    return answer
