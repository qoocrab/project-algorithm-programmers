#예상 시간 복잡도 O(n) n arr length
def solution(arr, divisor):
    answer = []
    for i in arr:
        if i % divisor == 0:
            answer.append(i)
    if answer == []:
        answer.append(-1)
    else:
        answer.sort()
    return answer
