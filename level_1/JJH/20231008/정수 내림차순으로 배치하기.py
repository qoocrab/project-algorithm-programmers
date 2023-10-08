#예상 시간 복잡도 O(n) n의 자리수
def solution(n):
    answer = []
    n_str = str(n)
    for i in range(0, len(n_str)):
        answer.append(n_str[i])
    answer.sort(reverse=True)

    return int(''.join(answer))
