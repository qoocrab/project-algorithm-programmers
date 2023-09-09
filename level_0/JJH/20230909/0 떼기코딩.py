# 예상 시간복잡도: O(n)
def solution(n_str):
    answer = ''
    index = 0
    for i in range(0,len(n_str),1):
        if n_str[i] == '0':
            pass
        else:
            index = i
            break
    answer = n_str[index:]
    return answer
