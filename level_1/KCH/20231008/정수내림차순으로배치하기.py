# 예상 시간복잡도: O(N)
def solution(n):
    return int(''.join(sorted(str(n), reverse = True)))
