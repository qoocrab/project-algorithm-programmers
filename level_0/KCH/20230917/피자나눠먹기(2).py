# 예상 시간복잡도: O(N)
def solution(n):
    for i in range(n//6, n//6 + 36):
        if i and 6*i % n == 0:
            return i

# cf) math.gcd
