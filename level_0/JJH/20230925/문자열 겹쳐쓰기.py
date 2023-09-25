# 예상 시간 복잡도 O(n) n my_string length
def solution(my_string, overwrite_string, s):
    answer = ''.join(my_string[:s] + overwrite_string + my_string[s+len(overwrite_string):])
    return answer
