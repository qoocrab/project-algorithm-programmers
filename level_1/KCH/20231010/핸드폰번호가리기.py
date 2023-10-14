# 예상 시간복잡도: O(1)
def solution(phone_number):
    return '*'*(len(phone_number)-4) + phone_number[-4:]
