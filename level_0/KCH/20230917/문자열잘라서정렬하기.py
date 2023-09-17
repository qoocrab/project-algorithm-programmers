# 예상 시간복잡도: O(N)
def solution(myString):
    return sorted(list(filter(len,myString.split('x'))))
