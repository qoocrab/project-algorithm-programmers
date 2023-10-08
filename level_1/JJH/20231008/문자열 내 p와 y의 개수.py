# 예상 시간 복잡도 O(s)
def solution(s):
    answer = True
    p_num = s.count('p') + s.count('P')
    y_num = s.count('y') + s.count('Y')
    if p_num == y_num:
        answer = True
    else:
        answer = False

    return answer
