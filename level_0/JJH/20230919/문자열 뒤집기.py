# 예상 시간 복잡도 : O(n) n : my_string length
def solution(my_string, s, e):
    prev = my_string[:s]
    list = [my_string[i] for i in range(e,s-1,-1)]
    reverse = ''.join(list)
    post = my_string[e+1:]
    return ''.join([prev,reverse,post])
