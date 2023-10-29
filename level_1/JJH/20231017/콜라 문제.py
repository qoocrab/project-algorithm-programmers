# 예상 시간 복잡도 O(n)
def solution(a, b, n):
    answer = 0
    emptyBottle = n
    while emptyBottle >= a:
        newEmptyBottle = (emptyBottle // a) * b
        answer = answer + newEmptyBottle
        emptyBottle = emptyBottle % a + newEmptyBottle

    return answer
