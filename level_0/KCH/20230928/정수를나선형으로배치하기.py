# 예상 시간복잡도: O(N**2)
def solution(n):
    move = [(0,1), (1,0), (0,-1), (-1,0)]
    MAP = [[0 for _ in range(n)] for _ in range(n)]
    MAP[0][0] = 1
    ex, ey = 0, 0
    
    while MAP[ex][ey] < n*n:
        for i in range(4):
            tx, ty = move[i]
            
            while True:
                if not(0<=ex+tx<n and 0<=ey+ty<n and MAP[ex+tx][ey+ty] == 0):
                    break
                nx = ex + tx
                ny = ey + ty
                
                MAP[nx][ny] = MAP[ex][ey] + 1
                ex, ey = nx, ny
            
    return MAP

# cf)
# def solution(n):
#     answer = [[None for j in range(n)] for i in range(n)]
#     move = [[0, 1], [1, 0], [0, -1], [-1, 0]]
#     x, y, m = 0, 0, 0
#     for i in range(1, n**2 + 1):
#         answer[y][x] = i
#         if y + move[m][0] >= n or x + move[m][1] >= n or answer[y + move[m][0]][x + move[m][1]]:
#             m = (m + 1) % len(move)
#         y, x = y + move[m][0], x + move[m][1]
#     return answer
