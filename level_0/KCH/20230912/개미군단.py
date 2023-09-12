# 예상 시간복잡도: O(1)
def solution(hp):
    return hp//5 + (hp%5)//3 + hp%5%3
