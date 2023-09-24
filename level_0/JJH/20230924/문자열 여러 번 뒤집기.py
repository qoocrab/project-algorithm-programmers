def solution(my_string, queries):
    answer = [i for i in my_string]
    for s,e in queries:
        answer = answer[:s] + [answer[i] for i in range(e,s-1,-1)] + answer[e+1:]
    return ''.join(answer)
