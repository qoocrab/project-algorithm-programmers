# 예상 시간복잡도: O(n)
def solution(num_list):
    answer = 0
    even = ''
    odd = ''
    for i in num_list:
        if i % 2 == 0: # even
            even = even + str(i)
        else:
            odd = odd + str(i)
    answer = int(even) + int(odd)
    return answer
