# 예상 시간복잡도: O(N)
def solution(my_strings, parts):
    answer = ''
    for [s,e],string in zip(parts, my_strings):
        answer += string[s:e+1]
    return answer
