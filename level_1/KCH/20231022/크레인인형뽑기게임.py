# 예상 시간복잡도: O(NK)
def solution(board, moves):
    stack = []
    cnt = 0
    for move in moves:
        top_doll = None
        for i in range(len(board)): #find top_doll
            if board[i][move-1] != 0:
                top_doll = board[i][move-1]
                board[i][move-1] = 0
                break
                
        if top_doll:
            stack.append(top_doll)
            if len(stack) >= 2 and stack[-1] == stack[-2]:
                del stack[-2:]
                cnt += 2   
            
    return cnt
