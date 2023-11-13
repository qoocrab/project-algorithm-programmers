# 예상 시간 복잡도 O(n) n a length
def solution(a, b):
    return sum([a[i]*b[i] for i in range(0,len(a))])
