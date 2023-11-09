# 예상 시간복잡도: O(NlogN..)
def solution(s):
    res = [0,0]
    while s!='1':
        new_str = ''.join(['' if i =='0' else i for i in s])
        res[0] += 1
        res[1] += (len(s) - len(new_str))
        s = str(bin(len(new_str)))[2:]
                
    return res
