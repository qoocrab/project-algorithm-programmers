def solution(arr, query):
    answer = arr.copy()
    for i in range(0, len(query)):
        if i % 2 == 0:
            answer = answer[:query[i]+1]
        else:
            answer = answer[query[i]:]
    return answer
