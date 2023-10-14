# 예상 시간복잡도: O(log(a자릿수 + b자릿수)) ==> O(1)
def solution(a, b):
    return max(int(f'{a}{b}'), 2*a*b)
