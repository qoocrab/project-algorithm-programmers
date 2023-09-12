# 예상 시간복잡도: O(K), K: 자릿수 길이
def solution(n):
    return sum(list(map(int,list(str(n)))))
