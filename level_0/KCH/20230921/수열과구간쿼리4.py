# 예상 시간복잡도: O(N*K), K: 슬라이스 길이
def solution(arr, queries):
    for s, e, k in queries:
        for i in range(s, e+1):
            if i%k==0: arr[i] += 1
    return arr
