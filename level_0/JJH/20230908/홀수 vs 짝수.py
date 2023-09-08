# 예상 시간복잡도: O(n)
def solution(num_list):
    answer = 0
    odd_sum = 0
    even_sum = 0
    for i in range(0, len(num_list), 1):
        if (i + 1) % 2 == 0: # even
            even_sum = even_sum + num_list[i]
        else:
            odd_sum = odd_sum + num_list[i]

    if even_sum < odd_sum:
        answer = odd_sum
    else:
        answer = even_sum
    return answer
