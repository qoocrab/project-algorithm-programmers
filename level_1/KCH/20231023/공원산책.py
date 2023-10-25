# 예상 시간복잡도: O(N**2)
def find_start(park):
    for i in range(len(park)):
        for j in range(len(park[i])):
            if park[i][j] == 'S':
                return i, j
            
def solution(park, routes):
    dir_dict = {'E': (0,1), 'W': (0,-1), 'S': (1,0), 'N': (-1,0)}
    x, y = find_start(park)
    
    for i in routes:
        direction, cnt = i.split()
        nx, ny = x, y
        for _ in range(int(cnt)):
            nx += dir_dict[direction][0]
            ny += dir_dict[direction][1]

            if not(0<=nx<len(park) and 0<=ny<len(park[0]) and park[nx][ny] != 'X'):
                break
        else: x, y = nx, ny
        
    return [x, y]
