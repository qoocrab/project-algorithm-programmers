# 예상 시간 복잡도 O(n^2)
def solution(arr, queries):
    answer = []
    for i in queries:
        value = 1000001
        for m in range(i[0],i[1]+1):
            if arr[m] > i[2]:
                if arr[m] < value:
                    value = arr[m]
            else:
                pass
        if value == 1000001:
            answer.append(-1)
        else:
            answer.append(value)
    return answer
