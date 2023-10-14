# 예상 시간복잡도: O(N**2)
def solution(l, r):
    tmp = [i for i in range(l, r+1) if not set(str(i))-set(['5','0'])]
    return tmp if tmp else [-1]
