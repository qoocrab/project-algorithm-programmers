# 예상 시간복잡도: O(N**2)
import sys
def solution(keymap, targets):
    res = []
    keymap_idx = [sys.maxsize for _ in range(26)]
    
    for key in keymap:
        for i in range(len(key)):
            keymap_idx[ord(key[i]) - ord('A')] = min(keymap_idx[ord(key[i]) - ord('A')], i+1)
            
    op = lambda x: keymap_idx[ord(x) - ord('A')]
    for word in targets:
        tmp = []
        for char in word:
            if op(char) == sys.maxsize:
                res.append(-1)
                break
            tmp.append(op(char))
        else: res.append(sum(tmp))
        
    return res
