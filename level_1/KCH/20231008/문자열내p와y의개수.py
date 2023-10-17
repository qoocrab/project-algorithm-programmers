# 예상 시간복잡도: O(N)
def solution(s):    
    pcnt, ycnt = 0, 0
    for i in s:
        if i in ['p', 'P']:
            pcnt += 1
        if i in ['y', 'Y']:
            ycnt += 1
    return pcnt == ycnt

# cf) Counter
# c = Counter(s) -> c['Y'], c['y'], ...
