# 예상 시간복잡도: O(N)
def solution(order):
    return len([i for i in list(str(order)) if i in {'3','6','9'}])
