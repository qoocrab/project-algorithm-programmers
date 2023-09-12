# 예상 시간복잡도: O(N)
def solution(sides):
    a, b, c = sorted(sides)
    return -int(c < a+b)+2
