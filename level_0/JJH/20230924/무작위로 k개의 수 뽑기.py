# 예상 시간 복잡도 O(arr)
def solution(arr, k):
    answer = []
    i = 0
    while len(answer) < k:
        if i < len(arr):
            while i < len(arr):
                if len(answer) >= k:
                    break
                if arr[i] not in answer:
                    answer.append(arr[i])
                i = i + 1
        else:
           answer.append(-1)
    return answer
