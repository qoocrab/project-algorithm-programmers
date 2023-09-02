# 예상 시간복잡도: O(n)
def solution(n):
    answer = 0
    for i in range (1,n+1):
        if i % 2 == 0: # 짝수
            answer = answer + i

    return answer

