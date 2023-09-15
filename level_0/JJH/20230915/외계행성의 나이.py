# 예상 시간복잡도: O(m) m : integer length
def solution(age):
    answer = ''
    list = []
    while age // 10 > 0:
        list.append(age % 10)
        age = age // 10
    list.append(age % 10)
    answer = ''.join([chr(97 + list[i]) for i in range(len(list)-1,-1,-1)])
    return answer
