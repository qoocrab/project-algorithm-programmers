# 예상 시간 복잡도 O(n) before, after length
def solution(before, after):
    answer = 0
    before_list = [i for i in before]
    after_list = [i for i in after]
    before_list.sort()
    after_list.sort()
    if before_list == after_list:
        answer = 1

    return answer
