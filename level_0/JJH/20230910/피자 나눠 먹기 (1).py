# 예상 시간복잡도: O(n)
def solution(n):
    answer = 1
    while (n * answer) % 6 != 0:
        answer = answer + 1

    return (answer * n) // 6
