# 예상 시간 복잡도 O(n)
def solution(n):
    answer = []
    n_str = str(n)
    for i in range(len(n_str)-1,-1,-1):
        answer.append(int(n_str[i]))
    return answer