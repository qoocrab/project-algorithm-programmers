# 예상 시간복잡도: O(n) n : my_string
def solution(my_string):
    answer = [my_string[i:] for i in range(0,len(my_string))]
    answer.sort()
    return answer
