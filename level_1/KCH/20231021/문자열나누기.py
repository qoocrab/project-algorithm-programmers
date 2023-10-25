# 예상 시간복잡도: O(N**2)
def solution(s):
    s += '0'
    string_cnt = 0
    x = s[0]
    cnt = [1,0] # x, not x
    
    i = 1
    while i < len(s)-1:
        if s[i] == x: cnt[0] +=1 
        else: cnt[1] += 1
        
        if cnt[1] == cnt[0]:
            string_cnt += 1
            cnt = [0,0]
            x = s[i+1]
            
        i += 1
        
    return string_cnt + int(cnt[0] != cnt[1])
            
    
    