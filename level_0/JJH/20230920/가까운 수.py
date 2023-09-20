# 예상 시간 복잡도 O(n)
def solution(array, n):
    diff = 10000
    idx = 0
    for i in range(0, len(array)):
        if abs(array[i] - n) < diff:
            diff = abs(array[i] - n)
            idx = i
        elif abs(array[i] - n) == diff:
            if array[idx] < array[i]:
                pass
            else:
                idx = i

    return array[idx]
