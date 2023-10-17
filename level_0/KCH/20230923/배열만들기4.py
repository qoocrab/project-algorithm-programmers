# 예상 시간복잡도: O(N)
def solution(arr):
    stk = []
    i = 0
    
    while i<len(arr):
        if not stk:
            stk.append(arr[i])
        elif stk[-1]<arr[i]:
            stk.append(arr[i])
        else:
            stk.pop()
            continue
        i += 1
        
    return stk
