# 예상 시간 복잡도 O(n)
def solution(my_string):
    answer = 0
    list = []
    i = 0
    list_count = 0
    while i < len(my_string):
        if my_string[i].isalpha():
            i = i + 1
            pass
        else:
            m = 0
            list.append([])
            while i + m < len(my_string):
                if my_string[i + m].isdigit():
                    list[list_count].append(my_string[i + m])

                else:
                    list_count = list_count + 1
                    break
                m = m + 1
            i = i + m
    for i in list:
        answer = answer + int(''.join(i))
    return answer
