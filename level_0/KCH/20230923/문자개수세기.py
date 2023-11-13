# 예상 시간복잡도: O(N)
def solution(my_string):
    res = [0] * 52
    for char in my_string:
        if ord('A') <= ord(char) <= ord('Z'):
            res[ord(char)-ord('A')] += 1
        elif ord('a') <= ord(char) <= ord('z'):
            res[26+ord(char)-ord('a')] += 1
    return res
