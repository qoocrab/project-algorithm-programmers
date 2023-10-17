# 예상 시간복잡도: O(NlogN)...... ==내장함수 .count
def solution(s):
    res = ''
    sorted_s = sorted(set(s))
    d = dict.fromkeys(sorted_s)
    for char in s:
        if d[char]:
            d[char] += 1
        else: d[char] = 1
        
    for k,v in d.items():
        if v == 1: 
            res += k
    return res

# cf)
# def solution(s):
#     answer = ''
#     for c in 'abcdefghijklmnopqrstuvwxyz':
#         if s.count(c) == 1:
#             answer += c
#     return answer
