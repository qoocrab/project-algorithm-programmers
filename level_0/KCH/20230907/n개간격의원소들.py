# 예상 시간복잡도: O(N), (N/n)
def solution(num_list, n):
    return [num_list[i] for i in range(0,len(num_list),n)]
