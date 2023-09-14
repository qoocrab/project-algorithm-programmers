# 예상 시간복잡도: O(n^2) n : arr length
def solution(arr):
    answer = 1
    for i in range(0,len(arr[0])):
        for l in range(0,i+1):
            if arr[i][l] != arr[l][i]:
                answer = 0
                break
            else:
                pass
    return answer
