# 예상 시간복잡도: O(N)
def solution(numbers):
    numbers.sort()
    return max(numbers[-1] * numbers[-2], numbers[0] * numbers[1])
