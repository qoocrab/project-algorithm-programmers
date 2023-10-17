# 예상 시간복잡도: O(N)
def solution(age):
    return ''.join([ chr(ord(i)+49) for i in str(age)])
