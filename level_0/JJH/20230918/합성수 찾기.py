# 예상 시간 복잡도 : O(n^2)
def solution(n):
    answer = 0
    for i in range(1,n+1):
        for m in range(2,i):
            if i % m == 0:
                answer = answer + 1
                break
    return answer
