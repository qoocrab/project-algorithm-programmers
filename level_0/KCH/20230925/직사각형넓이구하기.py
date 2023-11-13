# 예상 시간복잡도: O(1)
def solution(dots):
    [x1, y1], [x2, y2], [x3, y3], [x4, y4] = dots
    mmx = min(x1, x2, x3, x4)
    mxx = max(x1, x2, x3, x4)
    mmy = min(y1, y2, y3, y4)
    mxy = max(y1, y2, y3, y4)
    
    return abs(mmx - mxx) * abs(mmy - mxy)

# cf) 오른쪽 위 : max(dots), 왼쪽 아래 : min(dots)
