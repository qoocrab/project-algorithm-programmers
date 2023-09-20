# 예상 시간 복잡도 O(n) n : arr length
def solution(arr, flag):
    answer = []
    for i in range(0, len(flag)):
        if flag[i] is True:
            for l in range(0, arr[i] * 2):
                answer.append(arr[i])
        else:
            for l in range(0, arr[i]):
                answer.pop()

    return answer
