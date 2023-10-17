# 예상 시간복잡도: O(1)
def solution(common):
    if common[2] + common[0] == 2*common[1]: #등차
        return common[-1] + common[1] - common[0]
    return common[-1] * common[1] // common[0]
