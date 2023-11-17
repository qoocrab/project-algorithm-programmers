# 예상 시간복잡도: O(N)
from collections import Counter

def solution(k, tangerine):
    t_dict = Counter(tangerine)
    res = 0
    
    for cnt in sorted(t_dict.values(), reverse = True):
        k -= cnt
        res += 1
        if k<=0: break
        
    return res
