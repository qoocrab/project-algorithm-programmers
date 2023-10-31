def solution(X, Y):
    answer = 0
    xy = set(X) & set(Y)
    if not xy:
        answer = "-1"
    elif len(xy) == 1 and "0" in xy:
        answer = "0"
    else:
        result = [n * min(X.count(n), Y.count(n)) for n in xy]
        result.sort(reverse=True)
        answer = ''.join(result)
    return answer