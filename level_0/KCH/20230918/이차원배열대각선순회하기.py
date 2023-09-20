# 예상 시간복잡도: O(N**2)
def solution(board, k):
    SUM = 0
    for i in range(min(k+1,len(board))):
        for j in range(min(len(board[0])-1,k-i), -1, -1):
            SUM += board[i][j]
    return SUM
