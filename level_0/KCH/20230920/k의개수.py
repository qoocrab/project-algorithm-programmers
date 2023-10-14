# 예상 시간복잡도: O(N*logK), K: num 자릿수
def solution(i, j, k):
    count = 0
    for num in range(i, j + 1):
        while num > 0:
            digit = num % 10
            if digit == k:
                count += 1
            num //= 10
    return count
