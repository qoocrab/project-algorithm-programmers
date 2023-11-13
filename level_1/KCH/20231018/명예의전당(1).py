# 예상 시간복잡도: O(N*K*logN)
import bisect
def solution(k, score):
    res = [score[0]]
    tmp = [score[0]]
    for i in range(1, len(score)):
        tmp.insert(bisect.bisect_left(tmp, score[i]), score[i])
        res.append(tmp[-k] if len(tmp) >= k else tmp[0])
    return res

# cf) heapq.nsmallest
# 예상 시간복잡도: O(N*K*logN)
# import heapq

# def solution(k, score):
#     tmp = []
#     answer = []

#     for i in score:
#         heapq.heappush(tmp, i)
#         answer.append(heapq.nlargest(k, tmp)[min(len(tmp)-1, k-1)])

#     return answer
