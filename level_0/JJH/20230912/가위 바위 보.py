# 예상 시간복잡도: O(n)
def solution(rsp):
    answer = ''
    for i in range(0,len(rsp)):
        if rsp[i] == '2':
            answer = answer + '0'
        elif rsp[i] == '0':
            answer = answer + '5'
        elif rsp[i] == '5':
            answer = answer + '2'
        else:
            pass
    return answer
