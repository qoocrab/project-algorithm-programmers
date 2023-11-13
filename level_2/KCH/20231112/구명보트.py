# 예상 시간복잡도: O(N)
def solution(people, limit):
    # 구명보트는 혼자타거나, 둘이타거나
    people.sort()
    res, inter_sum = 0, 0
    l_idx, r_idx = 0, len(people) -1 
    
    while l_idx < r_idx:
        inter_sum = people[l_idx] + people[r_idx]
        if inter_sum <= limit: 
            # 무거운사람 하나만 탈 수 있음
            l_idx += 1 
        # 무겁 + 뚱뚱 둘 다 보냄
        res += 1
        r_idx -= 1 
    return res + int(l_idx == r_idx) # limit보다 가벼운 사람 한명 남아있는 경우 + 1
