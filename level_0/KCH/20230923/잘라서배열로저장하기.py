# 예상 시간복잡도: O(N)
import math

def solution(my_str, n):
    return [my_str[n*i:n*i+n] for i in range(math.ceil(len(my_str)/n))]

# cf) == range(0, len(my_str), n)
