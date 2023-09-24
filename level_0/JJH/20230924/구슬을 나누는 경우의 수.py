# 예상 시간 복잡도 O(1)
import math

def solution(balls, share):
    answer = math.factorial(balls) // (math.factorial((balls - share)) * math.factorial(share))
    return answer
