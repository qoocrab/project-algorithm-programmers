 # 예상 시간복잡도: O(N)
def solution(numlist, n):
    return sorted(numlist, key=lambda x:(abs(x-n), -x))
