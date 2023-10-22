# 예상 시간 복잡도 O(n^(1/2))
def solution(n):
    tmp = []
    for i in range(1, int(n**(1/2)) + 1):
        if n % i == 0:
            tmp.append(i)
            if i != n // i:
                tmp.append(n // i)
            else:
                pass
    answer = sum(tmp)
    return answer
