# 예상 시간복잡도: O(N**2)
import sys
def solution(wallpaper):
    MIN_X, MIN_Y, MAX_X, MAX_Y = sys.maxsize, sys.maxsize, 0, 0
    for i in range(len(wallpaper)):
        for j in range(len(wallpaper[0])):
            if wallpaper[i][j] == '#':
                MIN_X = min(i, MIN_X)
                MIN_Y = min(j, MIN_Y)
                MAX_X = max(i, MAX_X)
                MAX_Y = max(j, MAX_Y)
                
    return MIN_X, MIN_Y, MAX_X+1, MAX_Y+1
