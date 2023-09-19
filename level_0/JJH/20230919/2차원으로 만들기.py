# 예상 시간 복잡도 O(n) n : num_list length
def solution(num_list, n):
    answer = [[]]
    for i in range(0, len(num_list) // n):
        if i > 0:
            answer.append([])
        for m in range(0, n):
            answer[i].append(num_list[i * (n) + m])

    return answer
