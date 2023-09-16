# 예상 시간복잡도: O(n) n : number length
def solution(number):
    # 각 자리수 합
    sum = 0
    for i in range(0,len(number)):
        sum = sum + int(number[i])
    answer = sum % 9
    return answer
