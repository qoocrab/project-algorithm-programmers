# 예상 시간 복잡도 : O(n) n : my_string length
def solution(my_string):
    answer = []
    for i in my_string:
        if i in ''.join(answer):
            pass
        else:
            answer.append(i)
    return ''.join(answer)
