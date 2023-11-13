# 예상 시간복잡도: O(N)
import sys
def solution(n, m):
    MAX = 0
    MIN = sys.maxsize
    for i in range(1, n*m+1):
        if i<=min(n,m) and n%i == 0 and m%i == 0: # 최대공약수
            MAX = max(MAX, i)
        if i>=max(n,m) and i%n == 0 and i%m == 0: # 최소공배수
            MIN = min(MIN, i)
            
    return [MAX, MIN]

## 유클리드호제법: https://velog.io/@jwisgenius/%EC%95%8C%EA%B3%A0%EB%A6%AC%EC%A6%98-%ED%8C%8C%EC%9D%B4%EC%8D%AC-%EC%B5%9C%EB%8C%80%EA%B3%B5%EC%95%BD%EC%88%98%EC%9C%A0%ED%81%B4%EB%A6%AC%EB%93%9C-%ED%98%B8%EC%A0%9C%EB%B2%95-%EC%B5%9C%EC%86%8C%EA%B3%B5%EB%B0%B0%EC%88%98
