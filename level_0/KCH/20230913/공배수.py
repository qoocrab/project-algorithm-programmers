# 예상 시간복잡도: O(1)
def solution(number, n, m):
    return int(number%n==0 and number%m==0)
