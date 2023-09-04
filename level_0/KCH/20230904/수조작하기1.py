# 예상 시간복잡도: O(N)
def solution(n, control):
    dictionary = {'w':1, 's':-1, 'd':10, 'a':-10}
    for char in control:
        n += dictionary[char]
    return n
