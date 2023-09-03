# 예상 시간복잡도: O(n)
def solution(num_list):
    multi, exp = 1, 0

    for num in num_list:
        multi *= num
        exp += num

    return int(multi < exp**2)
