# 예상 시간복잡도: O(N)
def solution(s, n):
    op_lower = lambda x: ord(x) + n - ord('z') + ord('a') -1 if ord(x) + n > ord('z') else ord(x) + n
    op_upper = lambda x: ord(x) + n - ord('Z') + ord('A') -1 if ord(x) + n > ord('Z') else ord(x) + n
    return ''.join([' ' if i== ' ' else (chr(op_lower(i)) if i.islower() else chr(op_upper(i))) for i in s])
