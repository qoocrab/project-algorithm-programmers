# 예상 시간복잡도: O(1)
def solution(str):
    return str[len(str)//2] if len(str)%2 else str[len(str)//2 -1:len(str)//2 +1]
