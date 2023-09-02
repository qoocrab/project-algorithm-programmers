# 예상 시간복잡도: O(n)
def solution(num_list):
    answer = 0
    mul = 1
    sub = 0
    for i in num_list:
        mul = mul * i
        sub = sub + i
    if mul < sub * sub:
        answer = 1
    else:
        answer = 0
    return answer
