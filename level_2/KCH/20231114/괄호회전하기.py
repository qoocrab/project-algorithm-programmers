# 예상 시간복잡도: O(NK), K: 부분 문자열 길이
def check(sub_s):
    stack =[]
    char = {')':'(', ']':'[', '}':'{'}
    for i in sub_s:
        if i in [')', '}', ']']:
            if not stack or stack.pop() != char[i]:
                return 0
        else: stack.append(i)
        
    return int(not stack)

def solution(s):
    ds = s+s
    res = 0
    
    for i in range(len(s)):
        sub_s = ds[i:i+len(s)]
        res += check(sub_s)
        
    return res

# cf) deque의 .rotate
