# 예상 시간 복잡도 O(n) n : arr length
def solution(arr):
    stk = []
    i = 0
    while i < len(arr):
        if stk == []:
            stk.append(arr[i])
            i = i + 1
        elif stk[len(stk)-1] < arr[i]:
            stk.append(arr[i])
            i = i + 1
        else:
            stk.pop()

    return stk
