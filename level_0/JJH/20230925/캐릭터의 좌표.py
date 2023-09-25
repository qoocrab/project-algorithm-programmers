# 예상 시간 복잡도 O(keyinput)
def solution(keyinput, board):
    curPosition = [0, 0]
    widthLimit = board[0] // 2
    heightLimit = board[1] // 2
    for i in keyinput:
        if i == 'left':
            if curPosition[0] - 1 >= -widthLimit:
                curPosition[0] = curPosition[0] - 1
        elif i == 'right':
            if curPosition[0] + 1 <= widthLimit:
                curPosition[0] = curPosition[0] + 1

        elif i == 'up':
            if curPosition[1] + 1 <= heightLimit:
                curPosition[1] = curPosition[1] + 1
        elif i == 'down':
            if curPosition[1] - 1 >= -heightLimit:
                curPosition[1] = curPosition[1] - 1
    return curPosition
