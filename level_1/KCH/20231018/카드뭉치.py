# 예상 시간복잡도: O(N)
def solution(cards1, cards2, goal):
    idx = 0
    
    while idx<len(goal):
        if len(cards1) > 0 and goal[idx] == cards1[0]:
            cards1.pop(0)
        elif len(cards2) > 0 and goal[idx] == cards2[0]:
            cards2.pop(0)
        else: return "No"
        idx += 1
        
    return "Yes"
