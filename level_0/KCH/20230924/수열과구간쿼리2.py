# 예상 시간복잡도: O(N*K), K: 슬라이스 길이
def solution(arr, queries):
    res = []
    for s, e, k in queries:
        tmp = arr[s:e+1]
        MIN = 1000000
        for t in tmp:
            if t>k: MIN = min(t, MIN)
        
        res.append(MIN if MIN<1000000 else -1)
    return res

# cf) 
# min(list(filter(lambda x: x > k, arr[s:e+1]))
