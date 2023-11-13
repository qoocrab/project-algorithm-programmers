def solution(score):
    answer = []
    for mat, eng in score:
        answer.append((mat + eng) / 2)
    list = answer.copy()
    rank = [0 for i in range(0,len(score))]
    i = 1
    while list != []:
        max = -1
        for m in range(0, len(list)): # find max
            if list[m] > max:
                max = list[m]
                idx = m
        count = answer.count(max)
        for m in range(0, len(answer)): # delete max value in list and rank
            if answer[m] == max:
                rank[m] = i
                list.remove(max)
        i = i + count
    return rank


