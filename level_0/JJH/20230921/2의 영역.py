#예상 시간 복잡도 O(n) n : arr length
def solution(arr):
    answer = []
    if 2 in arr:
        prev_idx = len(arr)
        post_idx = 0
        for i in range(0,len(arr)):
            if arr[i] == 2:
                if i < prev_idx:
                    prev_idx = i
                if post_idx < i:
                    post_idx = i
        answer = arr[prev_idx:post_idx+1]
    else:
        answer = [-1]
    return answer
