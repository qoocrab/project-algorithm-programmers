# 예상 시간복잡도: O(N)
def solution(arr, delete_list):
    return [i for i in arr if i not in delete_list]
