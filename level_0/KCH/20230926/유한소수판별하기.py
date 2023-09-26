# 예상 시간복잡도: O(N)
def solution(a, b):
    tb = b
    while b:=tb:
        if b%5==0:
            tb = b//5
        elif b%2==0:
            tb = b//2
            
        if tb == b: break
    
    return 2 - int(a%b==0)
