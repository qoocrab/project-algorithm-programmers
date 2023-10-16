# 예상 시간복잡도: O(N)
def solution(sizes):
    max_w, max_h = 0, 0
    for i in range(len(sizes)):
        rotate_w = sizes[i][1]
        rotate_h = sizes[i][0]
        w, h = sizes[i]
        if max(max_w, w) * max(max_h, h) > max(max_w, rotate_w) * max(max_h, rotate_h):
            w = rotate_w
            h = rotate_h
            
        max_w = max(max_w, w)
        max_h = max(max_h, h)
        
    return max_w * max_h

# cf1)
# def solution(sizes):
    # row = 0
    # col = 0
    # for a, b in sizes:
    #     if a < b:
    #         a, b = b, a
    #     row = max(row, a)
    #     col = max(col, b)
    # return row * col

# cf2) 
# solution = lambda sizes: max(sum(sizes, [])) * max(min(size) for size in sizes)
