# 예상 시간복잡도: O(n)
def solution(my_string):
    answer = ''
    for i in range(0,len(my_string)):
        if my_string[i] == 'a' or my_string[i] == 'e' or my_string[i] == 'i' or my_string[i] == 'o' or my_string[i] == 'u':
            pass
        else:
            answer = answer + my_string[i]
    return answer
