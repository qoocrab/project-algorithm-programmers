# 예상 시간복잡도: O(NlogN)
import itertools

def solution(nums):
    res = 0
    test_case = list(itertools.combinations(nums, 3))
    MAX = sum(max(list(test_case), key = lambda x: sum(x)))
    case = [True for _ in range(MAX + 1)]
    
    for i in range(2, MAX + 1):
        if case[i]:
            for j in range(i+i, MAX+1, i):
                case[j] = False
                
    for a, b, c in test_case:
        if case[a+b+c]:
            res += 1
            
    return res
