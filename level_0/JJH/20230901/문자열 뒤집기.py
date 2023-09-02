# 예상 시간복잡도: O(n)
def solution(my_string):
    answer = ''
    for i in range(len(my_string)-1, -1, -1):
        answer = answer + my_string[i]
    return answer
