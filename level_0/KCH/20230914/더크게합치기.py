# 예상 시간복잡도: O(log(a자릿수) + log(b자릿수)) ==> O(1)
def solution(a, b):
    return max(int(str(a)+str(b)), int(str(b)+str(a)))
