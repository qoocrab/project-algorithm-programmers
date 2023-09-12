# 예상 시간복잡도: O(N)
def solution(myString, pat):
    ABBA = {'A':'B','B':'A'}
    pat_ = ''
    for i in pat:
        pat_+=ABBA[i]
        
    return int(pat_ in myString)
