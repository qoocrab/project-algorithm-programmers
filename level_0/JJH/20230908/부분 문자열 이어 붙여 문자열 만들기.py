# 예상 시간복잡도: O(n)
def solution(my_strings, parts):
    answer = ''
    count = 0
    for i in range(0, len(parts), 1):
        s, e = parts[i]
        answer = answer + my_strings[i][s:e+1]
    return answer
