# 예상 시간복잡도: O(NlogN)
def solution(number, limit, power):
    res = 0
    for i in range(1, number+1):
        tmp = 0
        for j in range(1, int(i**0.5) + 1):
            if i%j==0: tmp += 2
            if i**0.5 == j: tmp -= 1
            if tmp > limit:
                res += power
                break
        else: res += tmp
    return res
