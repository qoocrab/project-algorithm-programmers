# 예상 시간 복잡도 O(n)
def solution(x, n):
    answer = []
    if x == 0:
        for i in range(0,n):
            answer.append(0)
    else:
        for i in range(x, x + x*n, x):
            answer.append(i)
    return answer
