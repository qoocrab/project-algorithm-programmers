# 예상 시간 복잡도 O(n)
def solution(n):
    answer = ["수" if i % 2 == 0 else "박" for i in range(0, n)]

    return ''.join(answer)
