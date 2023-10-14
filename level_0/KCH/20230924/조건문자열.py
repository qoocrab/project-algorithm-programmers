# 예상 시간복잡도: O(N)
def solution(ineq, eq, n, m):
    op = (ineq+eq).replace('!','')
    return int(eval(str(n)+op+str(m)))
