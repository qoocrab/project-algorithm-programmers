# 예상 시간복잡도: O(n)
def solution(my_string, alp):
    answer = ''
    for i in range(0,len(my_string), 1):
        if my_string[i] == alp:
            answer = answer + alp.upper()
        else:
            answer = answer + my_string[i]
    return answer
