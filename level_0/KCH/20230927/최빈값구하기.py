# 예상 시간복잡도: O(N)
def solution(array):
    visited = [0] * 1001
    for i in array:
        visited[i] += 1
    li = visited.index(max(visited))
    ri = len(visited) - visited[::-1].index(max(visited)) -1
    
    if li != ri : return -1
    else: return li
