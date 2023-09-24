# 예상 시간 복잡도 O(arr)
def solution(arr):
    answer = []
    for i in range(0, len(arr)):
        if answer == []:
            answer.append(arr[i])
        else:
            if answer[len(answer) - 1] == arr[i]:
                answer.pop()
            else:
                answer.append(arr[i])

    if answer == []:
        answer = [-1]
    return answer
