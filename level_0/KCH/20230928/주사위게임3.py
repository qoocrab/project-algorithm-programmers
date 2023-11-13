# 예상 시간복잡도: O(N)
def solution(a, b, c, d):
    num = set([a,b,c,d])
    if len(num) == 1:
        return 1111*a
    for i in num:
        if [a,b,c,d].count(i) == (3 or 2):
            tmp = num - set([i])
            if len(tmp) == 1:
                p, q = i, (num - set([i])).pop()
                return (10 * p + q)**2            
            if len(tmp) == 2:
                q, r = tmp
                return q*r
            rest = tmp.pop()
            return (i+rest)*abs(i-rest)
    return min([a,b,c,d])
