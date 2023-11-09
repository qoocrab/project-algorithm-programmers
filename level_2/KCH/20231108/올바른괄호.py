# 예상 시간복잡도: O(N)
def solution(s):
    stack = []
    for i in s:
        if i ==')' and stack:
            stack.pop()
        else:
            stack.append(i)
    return len(stack) ==0
