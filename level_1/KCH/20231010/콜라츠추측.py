# 예상 시간복잡도: O(N)
def solution(num):
    if num==1: return 0
    for i in range(500):
        if num == 1: return i
        if num%2:
            num *= 3
            num += 1
        else: num//=2
        
    return -1
