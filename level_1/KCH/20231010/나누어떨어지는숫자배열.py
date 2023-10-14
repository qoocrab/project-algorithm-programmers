# 예상 시간복잡도: O(N)
def solution(arr, divisor):
    ans = [i for i in arr if i%divisor==0]
    return sorted(ans) if ans else [-1]
