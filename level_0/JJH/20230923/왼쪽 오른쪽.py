# 예상 시간 복잡도 O(n) n : str_list
def solution(str_list):
    answer = []
    l_idx = 21
    r_idx = 21
    if 'l' in str_list:
        l_idx = str_list.index('l')
    if 'r' in str_list:
        r_idx = str_list.index('r')

    if l_idx == 21 and r_idx == 21:
        answer = []
    elif l_idx < r_idx:
        answer = str_list[:l_idx]
    elif r_idx < l_idx:
        answer = str_list[r_idx+1:]

    return answer
