# 예상 시간 복잡도 O(1)
def solution(s):
    sign = 1
    number = 0
    if (s[0].isdigit()):
        number = int(s)
    else:
        if s[0] == "+":
            pass
        else:
            sign = -1
        number = int(s[1:]) * sign

    return number
