# 예상 시간복잡도: O(N*K), K: .index()
def solution(emergency):
    return [sorted(emergency, reverse=True).index(i)+1 for i in emergency]
