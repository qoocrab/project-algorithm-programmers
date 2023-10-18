def solution(k, score):
    answer = []

    for i in range(1, len(score)+1):
        tmp = score[:i]
        tmp.sort(reverse=True)
        if i <= k-1:
            answer.append(tmp[-1])
        else:
            answer.append(tmp[k-1])
    return answer
