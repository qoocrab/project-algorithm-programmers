# 예상 시간복잡도: O(N)
def solution(strArr):
    return [ strArr[i].lower() if i%2 == 0 else strArr[i].upper() for i in range(len(strArr))]
