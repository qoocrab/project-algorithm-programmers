# 예상 시간 복잡도 O(n) n : queries length
def solution(arr, queries):
    answer = arr
    for i in queries:
        tmp = answer[i[0]]
        answer[i[0]] = answer[i[1]]
        answer[i[1]] = tmp
    return answer
