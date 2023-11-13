# 예상 시간복잡도: O(K*N**2)... K: move 길이
def check(board, sx, sy):
    cnt = 1
    n = len(board)
    move = {(-1,0), (0,1), (0,-1), (1,0), (1,1), (-1,1), (1,-1), (-1,-1)}
    for tx, ty in move:
        nx = sx + tx
        ny = sy + ty
        
        if 0<=nx<n and 0<=ny<n and board[nx][ny] ==0:
            cnt += 1
            board[nx][ny] = 2
    return cnt

def solution(board):
    total = 0
    n = len(board)
    for i in range(n):
        for j in range(n):
            if board[i][j] == 1:
                total += check(board, i, j)
    return n*n - total
