# 예상 시간복잡도: O(N)
def solution(polynomial):
    xx, el = 0, 0
    for i in polynomial.split(' + '):
        if i[-1] == 'x':
            if i[:-1] == '':  xx += 1
            else: xx += int(i[:-1])
        else:
            el += int(i)
    
    if el and xx:
        if xx == 1: xx = ''
        return f'{xx}x + {el}'
    elif el:
        return f'{el}'
    else:
        if xx == 1: xx = ''
        return f'{xx}x'
