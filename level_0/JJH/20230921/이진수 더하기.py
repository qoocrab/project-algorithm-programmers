# 예상 시간 복잡도 O(1)
def solution(bin1, bin2):
    a = int(bin1,2)
    b = int(bin2,2)
    return str(bin(a+b))[2:]
