def solution(A, B):
    answer = -1
    string = [i for i in A]
    for i in range(0, len(A)+1):
        if ''.join(string) == B:
            answer = i
            break
        string = [string[-1]] + string[:len(A)-1]

    return answer

print(solution("abc", "bca"))
