# 예상 시간복잡도: O(N)
def solution(code):
    mode, ret = 0, ''
    for i in range(len(code)):
        if code[i] == '1':
            mode = (mode+1)%2 ## mode ^= 1
            
        elif (mode + i)%2==0:
            ret += code[i]

    return ret if ret else "EMPTY"
