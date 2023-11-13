# 예상 시간복잡도: O(N)
def solution(n):
    cnt = 0
    while n:
        if n%2: 
            cnt += 1
            n -= 1
        else:
            n//=2
            
    return cnt

# cf) bin(n).count('1') 
