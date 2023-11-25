# 예상 시간복잡도: O(NK), K: alpha_dict 길이
def solution(msg):
    s_idx, e_idx = 0, 1
    alpha_dict = {chr(ord('A') + i):i+1 for i in range(26)}
    res = []
    msg += 'z'
    
    w = msg[s_idx]
    while s_idx<len(msg)-1:
        if w in alpha_dict:
            w += msg[e_idx]
            e_idx += 1
            
        if w not in alpha_dict:
            res.append(alpha_dict[w[:-1]])
            s_idx = e_idx -1
            alpha_dict[w] = len(alpha_dict) + 1
            w = msg[s_idx]
            
    return res
