# 예상 시간복잡도: O(N)
def solution(q, r, code):
    return ''.join(code[i] for i in range(r, len(code), q))

## cf) == [r::q]
