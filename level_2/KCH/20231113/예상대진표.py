# 예상 시간복잡도: O(logN)
def solution(n,a,b):
    res = 1
    if b<a: a,b = b,a
    
    while n>2:
        if a%2 and abs(a-b) == 1:  #만남
            break
        a, b = (a-1)//2 + 1, (b-1)//2 + 1
        
        res += 1
        n//=2
    return res
