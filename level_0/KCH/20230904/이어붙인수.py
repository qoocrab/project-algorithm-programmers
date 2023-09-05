# 예상 시간복잡도: O(N)
# int 형변환 시간복잡도 : https://www.acmicpc.net/board/view/106721
def solution(num_list):
    even, odd = '', ''
    for i in num_list:
        if i%2 == 0:
            even += str(i)
        else:
            odd += str(i)
    return int(even) + int(odd)
