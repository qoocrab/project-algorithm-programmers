# 예상 시간복잡도: O(N**K), K: 10
from collections import Counter
def solution(want, number, discount):
    cnt = 0
    to_find = dict()
    for i in range(len(want)):
        to_find[want[i]] = number[i]
        
    for i in range(len(discount)):
        rest = Counter(discount[i:i+10])
        if to_find == rest: cnt += 1
        
    return cnt
