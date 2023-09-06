# 예상 시간복잡도: O(N)
def solution(num_list):
    accm_sum = 0
    accm_mul = 1
    for i in range(len(num_list)):
        accm_sum += num_list[i]
        if i<10:
            accm_mul *= num_list[i]
            
    return accm_sum if len(num_list)>10 else accm_mul

### cf) reduce
from functools import reduce
def solution(l):
    return sum(l) if len(l)>=11 else reduce(lambda a,b: a*b, l)
