# 예상 시간복잡도: O(N)
def solution(num_list, n):
    return num_list[n:] + num_list[:n]
