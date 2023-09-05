# 예상 시간복잡도: O(n)
def solution(num_list):
    answer = 0
    if len(num_list) > 10:
        for i in num_list:
            answer = answer + i
    else:
        answer = 1
        for i in num_list:
            answer = answer * i
    return answer
