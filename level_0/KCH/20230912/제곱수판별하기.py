# 예상 시간복잡도: O(1)
import math
def solution(n):
    return -int(math.sqrt(n)%1 == 0) + 2
