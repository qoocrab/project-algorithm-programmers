# 예상 시간 복잡도 O(n) n is t length - p length + 1
def solution(t, p):
    list = [t[i:i + len(p)] for i in range(0, len(t) - len(p) + 1) if int(t[i:i + len(p)]) <= int(p)]

    return len(list)
