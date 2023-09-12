# 예상 시간복잡도: O(N)
def solution(str_list, ex):
    res = ''
    for string in str_list:
        if ex in string:
            continue
        res+=string
    return res
