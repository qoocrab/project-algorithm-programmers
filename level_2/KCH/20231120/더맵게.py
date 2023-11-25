# 예상 시간복잡도: O(NlogN)
import heapq

def solution(scoville, K):
    cnt = 0
    heapq.heapify(scoville)
    while len(scoville) > 1:
        a = heapq.heappop(scoville)
        if a >= K: return cnt
        b = heapq.heappop(scoville)
        heapq.heappush(scoville, a+2*b)
        cnt += 1
    return -1 if scoville[0] < K else cnt
