#예상 시간 복잡도 O(n) n = |b-a|
def solution(a, b):
    answer = sum([i for i in range(min(a,b), max(a,b)+1)])
    return answer
