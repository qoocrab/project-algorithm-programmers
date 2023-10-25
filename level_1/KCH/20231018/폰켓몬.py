# 예상 시간복잡도: O(N)
def solution(nums):
    return min(len(nums)//2, len(set(nums)))
