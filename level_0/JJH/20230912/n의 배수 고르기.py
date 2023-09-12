# 예상 시간복잡도: O(n)
def solution(n, numlist):
    answer = []
    for i in numlist:
        if i % n == 0:
            answer.append(i)
    return answer
