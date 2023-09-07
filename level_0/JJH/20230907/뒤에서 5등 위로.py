# 예상 시간복잡도: O(n)
def solution(num_list):
    num_list.sort()
    answer = num_list[5:]
    return answer
