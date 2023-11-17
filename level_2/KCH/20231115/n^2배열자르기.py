# 예상 시간복잡도: O(N**2)
def solution(n, left, right):
    arr = []
    for i in range(left//n, right//n+1):
        arr += [i+1 if i>j else j+1 for j in range(n)]
    
    return arr[left%n:right - left + left%n + 1] 
