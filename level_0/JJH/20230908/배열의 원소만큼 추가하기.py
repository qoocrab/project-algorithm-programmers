# 예상 시간복잡도: O(n2)
def solution(arr):
    answer = []
    for i in arr:
        for m in range(0,i):
            answer.append(i)
    return answer
