# 예상 시간 복잡도 O(n) n is rank length
def solution(rank, attendance):
    list = []
    answer = 0
    for i in range(1, len(rank) + 1):
        if attendance[rank.index(i)]:
            list.append(rank.index(i))

    answer = 10000 * list[0] + 100 * list[1] + list[2]
    return answer
