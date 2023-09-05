# 예상 시간복잡도: O(n)
def solution(num_list):
    answer = -1
    count = 0
    for i in num_list:
        if i < 0:
            answer = count
            break;
        count = count + 1
    return answer
