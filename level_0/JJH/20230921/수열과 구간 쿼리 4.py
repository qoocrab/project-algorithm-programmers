# 예상 시간 복잡도 : O(s)
def solution(arr, queries):
    answer = arr.copy()
    for i in queries:
        for m in range(i[0], i[1] + 1):
            if m % i[2] == 0:
                answer[m] = answer[m] + 1

    return answer
