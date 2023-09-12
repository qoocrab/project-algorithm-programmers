# 예상 시간복잡도: O(N)
def solution(rsp):
    rsp_dict = {'2':'0', '0':'5', '5':'2'}
    return ''.join([rsp_dict[i] for i in rsp])
