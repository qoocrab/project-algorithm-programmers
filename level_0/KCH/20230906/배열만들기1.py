# 예상 시간복잡도: O(K), K : n/k(생성된 리스트 길이)
def solution(n, k):
    return list(range(1*k,n+1,k))
