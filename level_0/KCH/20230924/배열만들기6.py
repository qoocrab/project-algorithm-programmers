# 예상 시간복잡도: O(N)
def solution(arr):
    stk = []
    for i in range(len(arr)):
        if stk and stk[-1] == arr[i]:
            stk.pop()
        else:
            stk.append(arr[i])
    return stk if stk else [-1]

# cf) return stk or [-1]
