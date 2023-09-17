# 예상 시간복잡도: O(N)
def solution(a, d, included):
    return sum([a + i*d for i in range(len(included)) if included[i]])
