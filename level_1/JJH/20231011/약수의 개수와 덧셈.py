# 예상 시간 복잡도 O(n^2)
def solution(left, right):
    answer = 0
    for k in range(left, right + 1):
        if countDivisor(k) % 2 == 0:
            answer = answer + k
        else:
            answer = answer - k

    return answer


def countDivisor(n):
    tmp = 0
    for i in range(1, int(n ** (1 / 2)) + 1):
        if n % i == 0:
            if n / i == i:
                tmp = tmp + 1
            else:
                tmp = tmp + 2

    return tmp
