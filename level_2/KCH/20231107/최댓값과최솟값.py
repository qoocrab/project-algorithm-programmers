# 예상 시간복잡도: O(N)
import sys
def solution(s):
    MIN, MAX = sys.maxsize, -sys.maxsize
    
    for i in s.split():
        MIN = min(MIN, int(i))
        MAX = max(MAX, int(i))
        
    return f'{MIN} {MAX}'

def solution(s):
    s = list(map(int,s.split()))
    return f'{min(s)} {max(s)}'
