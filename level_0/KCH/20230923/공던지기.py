# 예상 시간복잡도: O(1)
def solution(numbers, k):
    return numbers[(2*(k-1))%len(numbers)]
