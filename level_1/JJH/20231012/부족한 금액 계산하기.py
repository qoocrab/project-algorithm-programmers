#예상 시간 복잡도 O(n) n is price
def solution(price, money, count):
    answer = -1
    requiredPrice = getPrice(count, price)
    answer = money - requiredPrice
    if answer >= 0:
        answer = 0

    return abs(answer)


def getPrice(count, price):
    priceList = [price * i for i in range(1, count + 1)]
    return sum(priceList)
