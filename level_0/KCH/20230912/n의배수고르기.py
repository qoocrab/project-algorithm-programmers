# 예상 시간복잡도: O(N)
def solution(n, numlist):
    return [i for i in numlist if i%n == 0]
