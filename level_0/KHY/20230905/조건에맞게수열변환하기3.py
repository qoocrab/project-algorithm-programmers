# 예상 시간복잡도: O(n)
def solution(arr, k):
    operation = lambda x: x * k if k % 2 else x + k
    return [operation(num) for num in arr]
