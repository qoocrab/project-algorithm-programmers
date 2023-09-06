# 예상 시간복잡도: O(N)
## iter 하나하나 순회하기 때문에 list() 시간복잡도 : O(N)
def solution(start, end_num):
    return list(range(start, end_num-1, -1))
