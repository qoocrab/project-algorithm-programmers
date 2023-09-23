#예상 시간 복잡도 O(n) n my_str length
def solution(my_str, n):
    answer = [my_str[i:i+n] for i in range(0,len(my_str),n)]
    return answer
