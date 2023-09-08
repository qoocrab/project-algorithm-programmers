# 예상 시간복잡도: O(n)
def solution(str_list, ex):
    answer = ''
    for i in str_list:
        if i.find(ex) >= 0:
            pass
        else:
            answer = answer + i
    return answer
