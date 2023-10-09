# 예상 시간복잡도: O(N)
def solution(numbers):
    return sum(set(range(1,10)) - set(numbers))

# O(1)
def solution(numbers):
    return sum(range(1,10)) - sum(numbers)
