# 예상 시간복잡도: O(N)
import itertools
def solution(number):
    op = lambda x: 1 if sum(x) == 0 else 0
    return sum([op(x) for x in itertools.combinations(number, 3)])
