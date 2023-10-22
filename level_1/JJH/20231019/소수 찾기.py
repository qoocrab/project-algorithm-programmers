# 예상 시간 복잡도 O(n^(3/2))

def solution(n):
    answer = 0
    for i in range(2,n+1):
        Found = True
        for m in range(2,int(i**(1/2) + 1)):
            if i % m == 0:
                Found = False
                break
        if Found:
            answer = answer + 1
    return answer
