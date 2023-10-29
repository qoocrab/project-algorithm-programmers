# 예상 시간 복잡도 O(n) n is size of Photo
def solution(name, yearning, photo):
    answer = []
    for i in range(0,len(photo)):
        tmp = []
        for k in range(0,len(photo[i])):
            if photo[i][k] in name:
                tmp.append(yearning[name.index(photo[i][k])])
            else:
                pass
        answer.append(sum(tmp))
    return answer
