# 예상 시간복잡도: O(N)
def solution(balls, share):
    res = 1
    share = min(share, balls - share)
    
    for i in range(share):
        res *= (balls-i)
        res /= (i+1)
    return res

# cf) from math import factorial as f
# cf) math.comb(balls, share)
