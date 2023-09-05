# 예상 시간복잡도: O(k), k: control 문자열의 길이
def solution(n, control):
    operations = {"w": 1, "s": -1, "d": 10, "a": -10}

    for c in control:
        n += operations[c]

    return n
