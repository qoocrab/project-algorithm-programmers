# 예상 시간복잡도: O(n^2) n : numbers length
def solution(numbers):
    max = -10000 * 10000 # max = 0 으로 하면 안됨! 원소들의 가능한 모든 곱들이 0보다 작은경우 존재
    for i in range(0,len(numbers)):
        for m in range(0,len(numbers)):
            if i != m:
                if numbers[i] * numbers[m] > max:
                    max = numbers[i] * numbers[m]
    return max
