# 예상 시간복잡도: O(n) n : intervals length
def solution(arr, intervals):
    answer = []
    for i in intervals:
        answer = answer + arr[i[0]:i[1]+1]
    return answer
