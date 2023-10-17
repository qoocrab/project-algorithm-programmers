# 예상 시간 복잡도 O(n) n arr1 size
def solution(arr1, arr2):
    answer = []
    for i in range(0, len(arr1)):
        answer.append([])
        for m in range(0, len(arr1[0])):
            answer[i].append(arr1[i][m] + arr2[i][m])
    return answer
