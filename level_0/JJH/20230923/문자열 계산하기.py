# 예상 시간 복잡도 O(n) n my_string length
def solution(my_string):
    command = my_string.split()
    answer = int(command[0])
    for i in range(1,len(command),2):
        if command[i] == '-':
            answer = answer - int(command[i+1])
        else:
            answer = answer + int(command[i+1])
    return answer
