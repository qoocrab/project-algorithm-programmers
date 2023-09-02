# 예상 시간복잡도: O(1)
def solution(slice, n):
    return n//slice + (0 if n%slice == 0 else 1)
