# 예상 시간복잡도: O(N)
import collections

def solution(maps):
    q = collections.deque()
    q.append((0,0,0))
    move = {(-1,0), (0,1), (1,0), (0,-1)}
    
    while q:
        cx,cy,cnt = q.popleft()
        if (cx,cy) == (len(maps)-1, len(maps[0]) -1):
            return cnt+1
        
        for tx, ty in move:
            nx = tx + cx
            ny = ty + cy
            
            if 0<=nx<len(maps) and 0<=ny<len(maps[0]) and maps[nx][ny] == 1:
                q.append((nx,ny,cnt+1))
                maps[nx][ny] = 2 # visited
    
    return -1 
