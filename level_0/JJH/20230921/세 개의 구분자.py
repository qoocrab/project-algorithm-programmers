# 예상 시간 복잡도 : O(n) n : myStr length
def solution(myStr):
    tmp = []
    for i in myStr:
        if i == 'a' or i == 'b' or i == 'c':
            tmp.append(' ')
        else:
            tmp.append(i)
    list =  ''.join(tmp).split()
    if list == []:
        answer = ['EMPTY']
    else:
        answer = list

    return answer
