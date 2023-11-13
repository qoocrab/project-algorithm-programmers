# 예상 시간 복잡도 O(n)
def solution(n):
    answer = 0
    trd_number = deciToTrd(n)
    revert = str(trd_number)[::-1]
    deci_number = trdToDeci(int(revert))
    return deci_number


def deciToTrd(dec):
    remain = dec
    result = []
    maxRank = 0
    for i in range(0, dec):
        if dec < 3 ** i:
            maxRank = i - 1
            break
    for k in range(maxRank, -1, -1):
        result.append(str(remain // 3 ** k))
        remain = remain % 3 ** k

    return int(''.join(result))


def trdToDeci(trd):
    result = 0
    trdString = str(trd)
    for i in range(1, len(trdString) + 1):
        result = result + (3 ** (len(trdString) - i) * int(trdString[i - 1]))
    return result

