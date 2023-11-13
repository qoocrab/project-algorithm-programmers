# 예상 시간복잡도: O(NK), K: 슬라이스 길이
def solution(array, commands):
    return [sorted(array[i-1:j])[k-1] for i, j, k in commands]
