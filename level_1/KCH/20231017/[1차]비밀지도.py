# 예상 시간복잡도: O(N)
def solution(n, arr1, arr2):
    op = lambda x: '#' if x == '1' else ' '
    for i in range(len(arr1)):
        total_map = str(bin(arr1[i] | arr2[i]))[2:].zfill(n)
        arr1[i] = ''.join([op(i) for i in total_map])
    return arr1
