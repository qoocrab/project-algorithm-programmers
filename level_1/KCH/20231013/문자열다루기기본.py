# 예상 시간복잡도: O(N)
def solution(s):
    if (len(s)==4) | (len(s)==6):
        if s.isdigit() : return True
    return False
