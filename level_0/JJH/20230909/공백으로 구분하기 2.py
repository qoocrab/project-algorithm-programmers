# 예상 시간복잡도: O(n)
def solution(my_string):
    answer = []
    sub_string = ''
    for i in range(0,len(my_string),1):
        if my_string[i] == ' ':
            if sub_string == '':
                pass
            else:
                answer.append(sub_string)
                sub_string = ''
        else:
            sub_string = sub_string + my_string[i]

    if sub_string != '': # flush sub_string to answer
        answer.append(sub_string)
    return answer

print(solution('i   love   you'))