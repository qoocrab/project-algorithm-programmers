# 예상 시간복잡도: O(N)
def solution(numbers):
    max_1, max_2 = sorted(numbers)[-1], sorted(numbers)[-2]
    return max_1 * max_2
