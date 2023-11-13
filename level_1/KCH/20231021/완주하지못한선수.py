# 예상 시간복잡도: O(N)
import heapq

def solution(participant, completion):
    heapq.heapify(participant)
    heapq.heapify(completion)
    for i in range(len(completion)):
        n1 = heapq.heappop(participant)
        n2 = heapq.heappop(completion)
        
        if n1 != n2:
            return n1
        
    return participant[0]
        
