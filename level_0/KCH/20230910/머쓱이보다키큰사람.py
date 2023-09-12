# 예상 시간복잡도: O(N)
def solution(array, height):
    return len([i for i in array if i > height])
