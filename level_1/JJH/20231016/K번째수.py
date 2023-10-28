# 예상 시간 복잡도 O(n) n command length
def solution(array, commands):
    answer = []
    for i in range (0,len(commands)):
        tmp = array[commands[i][0]-1:commands[i][1]]
        tmp.sort()
        answer.append(tmp[commands[i][2]-1])
    return answer
