# 예상 시간복잡도: O(N)
def solution(s):
    word = {
        'zero':'0',
        'one':'1',
        'two':'2',
        'three':'3',
        'four':'4',
        'five':'5',
        'six':'6',
        'seven':'7',
        'eight':'8',
        'nine':'9'
    }
    res, tmp = '', ''
    for i in range(len(s)):
        if not s[i].isdigit():
            tmp += s[i]
            try:
                res += word[tmp]
                tmp = ''
                continue
            except:
                continue
        
        res += s[i]
    return int(res)
