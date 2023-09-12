# 예상 시간복잡도: O(N)
def solution(num_list):
    odd, even = 0, 0
    for i in range(len(num_list)):
        if i%2==0:
            even += num_list[i]
        else: odd += num_list[i]
    return max(even, odd)
