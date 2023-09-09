# 예상 시간복잡도: O(n)
def solution(arr, n):
    answer = []
    if len(arr) % 2 == 0: # even case
        count = 0
        for i in arr:
            if count % 2 == 0: # even Elements
                answer.append(i)
            else:
                answer.append(i + n)
            count = count + 1
    else:
        count = 0
        for i in arr:
            if count % 2 != 0:  # odd Elements
                answer.append(i)
            else:
                answer.append(i + n)
            count = count + 1

    return answer
