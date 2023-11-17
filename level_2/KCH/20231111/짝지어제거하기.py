# 예상 시간복잡도: O(N)
def solution(s):
    stack = []
    for i in range(len(s)):
        if stack and stack[-1] == s[i]:
            stack.pop()
            continue
        stack.append(s[i])
    return int(len(stack) == 0)
