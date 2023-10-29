# 예상 시간 복잡도 O(n^2)
def solution(n, arr1, arr2):
    answer = []
    Map = []
    for i in range(0, n):
        map1 = intToBinaryString(arr1[i], n)
        map2 = intToBinaryString(arr2[i], n)
        tmp = []
        for k in range(0, n):
            if map1[k] == '1' or map2[k] == '1':
                tmp.append('#')
            else:
                tmp.append(' ')
        Map.append(''.join(tmp))

    return Map

def intToBinaryString(integer, n):
    tmp = str(bin(integer))
    tmp = tmp[2:]
    if n - len(tmp) > 0:
        tmp = ( "0" * (n - len(tmp))) + tmp
    return tmp
