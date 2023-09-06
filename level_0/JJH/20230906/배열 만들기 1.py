# 예상 시간복잡도: O(n)
def solution(n, k):
    answer = []
    for i in range(k,n+1,k):
        answer.append(i)
    return answer
