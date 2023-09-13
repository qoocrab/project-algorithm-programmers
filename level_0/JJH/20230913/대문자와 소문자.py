# 예상 시간복잡도: O(m) m : string length
def solution(my_string):
    answer = ''
    list = []
    for i in range(0, len(my_string)):
        if my_string[i].islower():
            list.append(my_string[i].upper())
        else:
            list.append(my_string[i].lower())
    answer = ''.join(list)
    return answer

print(solution('cccCCC'))