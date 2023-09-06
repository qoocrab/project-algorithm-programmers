# 예상 시간복잡도: O(n)
def solution(rny_string):
    answer = ''
    for i in range (0,len(rny_string),1):
        if rny_string[i] == 'm':
            answer = answer + 'rn'
        else:
            answer = answer + rny_string[i]
    return answer
