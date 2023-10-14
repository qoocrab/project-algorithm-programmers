# 예상 시간복잡도: O(logN)
def solution(n):
    res = ''
    while n:
        res += str(n%3)
        n //= 3
        
    return int(res,3)
