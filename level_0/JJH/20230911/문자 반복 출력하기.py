# 예상 시간복잡도: O(n^2)
def solution(my_string, n):
    answer = ''
    for i in range(0,len(my_string)):
        for m in range(0,n):
            answer = answer + my_string[i]
    return answer
