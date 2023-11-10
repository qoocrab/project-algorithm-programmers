# 예상 시간복잡도: O(NK)
def solution(n):
    next_num = n
    while True:
        next_num += 1
        if bin(n)[2:].count('1') == bin(next_num)[2:].count('1'):
            return next_num
