# 예상 시간복잡도: O(N)
def solution(array):
    return ''.join(list(map(str, array))).count('7')

## cf) str(array) == ''.join(list(map(str, array)))
