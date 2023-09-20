# 예상 시간복잡도: O(N)
def solution(num, k):
    try:
        return list(str(num)).index(str(k)) + 1
    except:
        return -1
