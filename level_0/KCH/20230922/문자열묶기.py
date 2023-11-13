# 예상 시간복잡도: O(N)
def solution(strArr):
    group_cnt = [0 for _ in range(30)]
    for word in strArr:
        group_cnt[len(word)-1] += 1
        
    return max(group_cnt)
