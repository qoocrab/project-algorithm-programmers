# 예상 시간복잡도: O(n)
from math import prod


def solution(num_list):
    if len(num_list) >= 11:
        return sum(num_list)
    elif len(num_list) <= 10:
        return prod(num_list)
