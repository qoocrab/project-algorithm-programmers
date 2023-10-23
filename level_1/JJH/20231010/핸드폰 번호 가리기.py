# 예상 시간 복잡도 O(n) n phone_number length
def solution(phone_number):
    answer = ''.join([phone_number[i] if i >= len(phone_number)-4 else "*" for i in range(0,len(phone_number))])
    return answer
