# 예상 시간 복잡도 O(n) n polynomial length
def solution(polynomial):
    list = polynomial.split()
    x_coef = 0
    integer = 0
    if 'x' in list[0]:
        if list[0] == 'x':
            x_coef = x_coef + 1
        else:
            x_coef = x_coef + int(list[0][:len(list[0]) - 1])
    else:
        integer = integer + int(list[0])
    for i in range(2, len(list), 2):
        if 'x' in list[i]:
            if  list[i] == 'x':
                x_coef = x_coef + 1
            else:
                x_coef = x_coef + int(list[i][:len(list[i])-1])
        else:
            integer = integer + int(list[i])

    answer = []
    if x_coef != 0:

        if x_coef == 1:
            answer.append('x')
        elif x_coef == -1:
            answer.append('-x')
        else:
            answer.append(str(x_coef) + "x")

        if integer != 0:

            answer.append(' + ')
            answer.append(str(integer))
        else:
            pass
    else:
        answer.append(str(integer))



    answer = ''.join(answer)
    return answer
