# 예상 시간복잡도: O(N)
import re
def solution(s):
    return sum(map(int,re.sub('-?\d+\sZ', ' ', s).split()))

## 정규표현식 X
# 예상 시간복잡도: O(N)
def solution(s):
    res = []
    for i in s.split():
        if i == 'Z':
            res.pop()
            continue
        res.append(int(i))
        
    return sum(res)
