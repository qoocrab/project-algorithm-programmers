# 예상 시간복잡도: O(n)
def solution(myString, pat):
    answer = 0
    myStringLower = myString.lower()
    patLower = pat.lower()
    if myStringLower.find(patLower) >= 0:
        answer = 1
    else:
        answer = 0
    return answer
