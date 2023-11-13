# 예상 시간복잡도: O(N)
def solution(numLog):
    status = {-1 : 'w', 1 : 's', -10 : 'd', 10:'a'}
    return ''.join([status[(numLog[i-1] - numLog[i])]for i in range(1, len(numLog))])
