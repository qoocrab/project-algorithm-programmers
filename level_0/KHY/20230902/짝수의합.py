# 예상 시간복잡도: O(1)
def solution(n):
    count = n // 2
    return 2 * (count * (count + 1) / 2)
