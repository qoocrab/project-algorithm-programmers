# 예상 시간복잡도: O(N)
def solution(absolutes, signs):
    op = lambda x, y: x if y else -x
    return sum([op(absolutes[i], signs[i]) for i in range(len(signs))])
