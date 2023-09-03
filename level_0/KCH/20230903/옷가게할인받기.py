# 예상 시간복잡도: O(1)
def solution(price):
    if price >= 500000: off = 0.8
    elif price >= 300000: off = 0.9
    elif price >= 100000 : off = 0.95
    else: off = 1
    return int(price*off)
