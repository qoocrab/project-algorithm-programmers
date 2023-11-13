# 예상 시간복잡도: O(N)
def solution(s, skip, index):
    diction = [chr(i+ord('a')) for i in range(26) if chr(i+ord('a')) not in skip]
    alpha = {diction[i]:i for i in range(len(diction))}
    res = ''
    for c in s:
        res += diction[(alpha[c] + index)%len(alpha)]
        
    return res
