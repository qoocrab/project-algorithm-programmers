# 예상 시간복잡도: O(N)
def solution(before, after):
    return int(sorted(before) == sorted(after))
