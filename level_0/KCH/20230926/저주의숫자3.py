# 예상 시간복잡도: O(N) ㅎㅎ,,
def solution(n):
    op = lambda x: x if x%3!=0 and '3' not in str(x) else None
    res = [op(i) for i in range(1, 200) if op(i)]
    return res[n-1]
