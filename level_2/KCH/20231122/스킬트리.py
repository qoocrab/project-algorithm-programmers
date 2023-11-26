# 예상 시간복잡도: O(N**2 K)...
def solution(skill, skill_trees):
    res = 0
    for tree in skill_trees:
        tmp = ''
        for char in tree:
            if char in skill:
                tmp += char
        if skill[:len(tmp)] == tmp: res += 1
        
    return res
