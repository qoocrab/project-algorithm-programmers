# 예상 시간 복잡도 O(n) n : my_string length
def solution(my_string, indices):
    answer = ''.join([my_string[i] for i in range(0,len(my_string)) if not i in indices])
    return answer
