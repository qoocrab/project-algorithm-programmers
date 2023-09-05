# 예상 시간복잡도: O(n)
def solution(numbers, n):
    sum = 0
    for i in numbers:
        sum = sum + i
        if sum > n:
            break
    return sum
