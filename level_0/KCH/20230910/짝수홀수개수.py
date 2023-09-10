# 예상 시간복잡도: O(N)
def solution(num_list):
    odd, even = 0, 0
    for i in num_list:
        if not i%2: even += 1
        else: odd += 1

    return [even, odd]
