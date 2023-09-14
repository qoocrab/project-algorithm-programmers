# 예상 시간복잡도: O(m) m : array length
def solution(arr, idx):
    answer = -1
    list = arr[idx:]
    for i in range(0,len(list)):
        if list[i] == 1:
            answer = idx + i
            break
    return answer
