# 예상 시간 복잡도 : O(n) n : quries length
def solution(arr, queries):
    answer = arr
    for i in queries:
        for k in range(i[0],i[1]+1):
            answer[k] = answer[k] + 1
    return answer
