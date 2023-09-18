# 예상 시간복잡도: O(N)
## https://school.programmers.co.kr/learn/courses/30/lessons/181905
def solution(my_string, s, e):
    tmp = list(my_string)
    tmp[s:e+1] = tmp[s:e+1][::-1]
    return ''.join(tmp)
