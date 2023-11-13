# 예상 시간복잡도: O(N)
def solution(keyinput, board):
    way = {'left' : (-1,0), 
           'right' : (1,0),
           'up' : (0,1),
           'down': (0,-1) }
    
    x, y = 0, 0
    
    for key in keyinput:
        tx, ty = way[key]
        nx, ny = x + tx, y + ty
        
        if -(board[0]//2)<=nx<=board[0]//2 and -(board[1]//2)<=ny<=board[1]//2:
            x, y = nx, ny
            
    return x,y
