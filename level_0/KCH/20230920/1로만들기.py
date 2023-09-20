# 예상 시간복잡도: O(N)
def find(num):
    tmp = 1
    for i in range(30):
        tmp *= 2
        if tmp > num:
            break
    return i

def solution(num_list):
    res = 0
    for num in num_list:
        res += find(num) 
    return res
