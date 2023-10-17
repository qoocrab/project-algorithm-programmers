# 예상 시간복잡도: O(N)
def solution(arr):
    idx = 0
    while True:
        op = lambda i: i//2 if i>=50 and i%2==0 else(i*2+1 if i%2==1 and i<50 else i)
        narr = [op(i) for i in arr]
        
        if narr != arr:
            arr = narr
            idx += 1
        else:
            return idx
