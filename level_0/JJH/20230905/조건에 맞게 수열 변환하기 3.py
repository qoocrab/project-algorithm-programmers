# 예상 시간복잡도: O(n)
def solution(arr, k):
    answer = []
    if k % 2 == 0: # even
        for i in arr:
            answer.append(i + k)
    else:
        for i in arr:
            answer.append(i * k)
    return answer
