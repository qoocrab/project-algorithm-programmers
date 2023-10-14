# 예상 시간복잡도: O(N)
def solution(s):
    res = ''
    s_idx = 0
    for char in range(len(s)):
        if s[char] == ' ': 
            res += s[char]
            s_idx = char+1
        else:
            res += s[char].lower() if (char-s_idx)%2 else s[char].upper()
    return res
