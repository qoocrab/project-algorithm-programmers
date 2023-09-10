# 예상 시간복잡도: O(n)
def solution(array, height):
    answer = 0
    for i in array:
        if height < i:
            break
        answer = answer + 1
    return len(array) - answer
