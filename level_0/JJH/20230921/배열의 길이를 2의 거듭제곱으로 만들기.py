# 예상 시간 복잡도 : O(n) n : arr length
def solution(arr):
    answer = []
    pow = 0
    while 2 ** pow < len(arr):
        pow = pow + 1

    answer = arr.copy()
    for i in range(len(arr), 2 ** pow):
        answer.append(0)
    return answer
