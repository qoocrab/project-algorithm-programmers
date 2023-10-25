# 예상 시간복잡도: O(N)
def solution(X, Y):
    chr_list_X = [0 for _ in range(10)]
    chr_list_Y = [0 for _ in range(10)]
    
    for i in X:
        chr_list_X[int(i)] += 1
    for i in Y:
        chr_list_Y[int(i)] += 1
    
    res = ''
    for i in range(9, -1, -1):
        res += str(i)*min(chr_list_X[i], chr_list_Y[i])
    
    if not res: res = '-1'
    return '0' if res[0] == '0' else res

# cf) from collections import Counter
