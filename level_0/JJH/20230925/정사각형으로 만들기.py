#예상 시간 복잡도 O(n) n arr length
def solution(arr):
    answer = []
    if len(arr) < len(arr[0]):
        answer = arr.copy()
        for i in range(0, len(arr[0]) - len(arr)):
            answer.append([0 for i in range(len(arr[0]))])
    else:
        for i in range(0, len(arr)):
            answer.append(arr[i] + [0 for i in range(0, len(arr) - len(arr[0]))])

    return answer
