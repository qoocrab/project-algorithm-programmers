# 예상 시간복잡도: O(1)
def solution(price):
    discounts = {500000: 0.80, 300000: 0.90, 100000: 0.95}

    for threshold, rate in discounts.items():
        if price >= threshold:
            return int(price * rate)

    return price
