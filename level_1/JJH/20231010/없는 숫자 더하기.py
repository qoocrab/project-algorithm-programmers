# 예상 시간 복잡도 O(n) numbers length
def solution(numbers):
    list = [i for i in range(0,10)]
    for i in numbers:
        list.remove(i)
    return sum(list)
