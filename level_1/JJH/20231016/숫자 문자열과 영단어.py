# 예상 시간 복잡도 O(n)
def solution(s):
    answer = []
    number = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
    tmp = []
    for i in s:
        if i.isdigit():
            answer.append(i)
        else:
            tmp.append(i)
            if ''.join(tmp) in number:

                answer.append(str(number.index(''.join(tmp))))
                tmp = []
            else:
                pass

    return int(''.join(answer))
