# 예상 시간복잡도: O(n^2)
def solution(n):
    answer = [[]]
    for i in range(0,n):
        for j in range(0,n):
            if i == j:
                answer[i].append(1)
            else:
                answer[i].append(0)
        if i < n-1:
            answer.append([])
    return answer
