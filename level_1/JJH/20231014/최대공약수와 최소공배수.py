# 예상 시간 복잡도 O(n)
def solution(n, m):
    answer = []
    for k in range(min(n, m), 0, -1):
        if n % k == 0 and m % k == 0:
            answer.append(k)
            break

    for i in range(min(n, m), (n * m) + 1):
        if i % n == 0 and i % m == 0:
            answer.append(i)
            break

    return answer
