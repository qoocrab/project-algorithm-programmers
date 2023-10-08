# 예샹 시간 복잡도 O(1)
def solution(n):
    answer = -1

    # check root exist
    sqrt = n ** (1 / 2)
    if sqrt == int(sqrt):
        answer = (sqrt + 1) ** 2
    else:
        pass
    return answer
