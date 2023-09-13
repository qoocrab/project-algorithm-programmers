# 예상 시간복잡도: O(m), m은 numbers 리스트의 길이
def solution(numbers, n):
    total = 0

    for num in numbers:
        total += num
        if total > n:
            return total

    return total
