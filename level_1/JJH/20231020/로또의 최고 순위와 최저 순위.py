# 예상 시간 복잡도 O(n^2)
def solution(lottos, win_nums):
    answer = []
    correct = 0
    for i in lottos:
        for k in win_nums:
            if i == k:
                correct = correct + 1
    zeros = lottos.count(0)

    if correct + zeros > 1:
        answer.append(7-correct-zeros)
    else:
        answer.append(6)
    if correct > 1:
        answer.append(7-correct)
    else:
        answer.append(6)
    return answer
