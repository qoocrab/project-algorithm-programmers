# 예상 시간복잡도: O(N)
def solution(lines):
    case = []
    for i in range(3):
        for j in range(i+1, 3):
            s1, e1 = lines[i]
            s2, e2 = lines[j]
            case.append([max(s1, s2), min(e1, e2)])
    visited = [0] * 201
    for s,e in case:
        if s>=e: continue
        for i in range(s,e):
            visited[i] = 1
    return sum(visited)
