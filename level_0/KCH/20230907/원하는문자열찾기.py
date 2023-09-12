# 예상 시간복잡도: O(N)
def solution(myString, pat):
    return int(pat.lower() in myString.lower())
