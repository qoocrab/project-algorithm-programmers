# 예상 시간복잡도: O(1)
def solution(price):
    answer = 0
    discount = 0
    if price >= 100000 and price < 300000:
        discount = 0.05
    elif price >= 300000 and price < 500000:
        discount = 0.1
    elif price >= 500000:
        discount = 0.2
    answer = price - (price * discount)
    return int(answer)

print(solution(580000))
