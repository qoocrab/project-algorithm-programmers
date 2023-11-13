# 예상 시간복잡도: O(N)
def solution(food):
    answer = ''
    for i in range(1, len(food)):
        answer += str(i) * (food[i]//2)
    return answer + '0' + answer[::-1]
