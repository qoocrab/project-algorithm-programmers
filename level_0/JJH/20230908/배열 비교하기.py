# 예상 시간복잡도: O(n)
def solution(arr1, arr2):
    answer = 0
    if len(arr1) < len(arr2):
        answer = -1
    elif len(arr1) > len(arr2):
        answer = 1
    else:
        arr1_sum = sum(arr1)
        arr2_sum = sum(arr2)
        if arr1_sum > arr2_sum:
            answer = 1
        elif arr1_sum < arr2_sum:
            answer = -1
        else:
            answer = 0

    return answer
