# 예상 시간복잡도: O(n^2)
def solution(numbers):
    list = numbers.copy()
    list.sort()
    answer = list[len(list)-1] * list[len(list)-2]
    return answer
