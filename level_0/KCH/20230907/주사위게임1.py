# 예상 시간복잡도: O(1)
def solution(a, b):
    if a%2==1 and b%2==1:
        return a**2 + b**2
    elif (a+b)%2 == 1:
        return 2*(a+b)
    else:
        return abs(a-b)
    