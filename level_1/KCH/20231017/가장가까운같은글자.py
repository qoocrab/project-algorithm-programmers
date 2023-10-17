# 예상 시간복잡도: O(N)
def solution(s):
    visited_idx = [-1 for _ in range(26)]
    res = []
    for i in range(len(s)):
        ex_idx = visited_idx[ord(s[i])-ord('a')]
        res.append(ex_idx if ex_idx == -1 else i+1 - ex_idx)
        visited_idx[ord(s[i])-ord('a')] = i+1
    return res
