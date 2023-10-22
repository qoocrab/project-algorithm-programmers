# 예상 시간 복잡도 O(n) n score size
def solution(k, m, score):
    answer = 0
    packageNum = len(score) // m
    score.sort(reverse=True)
    for i in range(m-1, (packageNum * m) + 1, m):
        answer = answer + score[i] * m

    return answer

print(solution(	4, 3, [4, 1, 2, 2, 4, 4, 4, 4, 1, 2, 4, 2]))