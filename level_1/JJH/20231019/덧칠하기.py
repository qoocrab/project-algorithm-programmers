def solution(n, m, section):
    answer = 0
    for i in section:
        for k in range(i, i + m):
            if k in section:
                section.remove(k)
        answer = answer + 1

    return answer

print(solution(8,4,[2,3,6]))