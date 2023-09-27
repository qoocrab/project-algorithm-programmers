# 예상 시간 복잡도 O(n) n code length
def solution(code):
    answer = []
    mode = False
    for i in range(0,len(code)):
        if code[i] == '1':
            mode = not mode
        else:
            if mode: # mode 1
                if i % 2 == 1:
                    answer.append(code[i])
                else:
                    pass
            else:
                if i % 2 == 0:
                    answer.append(code[i])
                else:
                    pass
    if answer == []:
        answer.append('EMPTY')
    return ''.join(answer)
