# 예상 시간복잡도: O(NK)
import sys
sys.setrecursionlimit(1000000) 

fib = [0] * 100001
fib[1] = 1
def solution(n):
    global fib
    if n<2 or fib[n]!=0: return fib[n]
    fib[n] = (solution(n-1) + solution(n-2))%1234567
    return fib[n]

# ㄷㄷ
def fibonacci(num):
    a, b = 0, 1
    for _ in range(num):
        a, b = b%1234567, a+b%1234567
    return a
