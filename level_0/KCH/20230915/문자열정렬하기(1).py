# 예상 시간복잡도: O(NlogN)
def solution(my_string):
    return sorted([int(i) for i in my_string if 47<ord(i)<58])
