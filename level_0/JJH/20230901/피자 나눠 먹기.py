# 예상 시간복잡도: O(1)
def solution(slice, n):
    answer = 0
    if n % slice != 0:
        answer = (n // slice) + 1
    else:
        answer = (n // slice)
    return answer
