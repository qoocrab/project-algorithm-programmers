# 예상 시간복잡도: O(N)
def solution(num, total):
    mean = total / num
    start = int(mean+0.5)-num//2
    return list(range(start,start+num))
