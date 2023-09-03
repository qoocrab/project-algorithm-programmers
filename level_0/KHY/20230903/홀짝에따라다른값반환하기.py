# 예상 시간복잡도: O(1)
def solution(n):
    if n % 2 == 1:
        return ((n + 1) // 2) ** 2
    else:
        return 4 * (n // 2) * ((n // 2) + 1) * (n + 1) // 6
