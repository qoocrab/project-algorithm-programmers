def solution(number):
    answer = 0
    list =[]
    for i in range(0,len(number)):
        for k in range(i+1,len(number)):
            for m in range(k+1,len(number)):
                if number[i] + number[k] + number[m] == 0:
                    tmp = [i, k, m]
                    if tmp in list:
                        pass
                    else:
                        list.append(tmp)
                        answer = answer + 1
    return answer

print(solution(	[-3, -2, -1, 0, 1, 2, 3]))