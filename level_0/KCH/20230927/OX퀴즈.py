# 예상 시간복잡도: O(NK), K: left 문자열 길이
def solution(quiz):
    res = ['O'] * len(quiz)
    for i in range(len(quiz)):
        left, right = quiz[i].split('=')
        if eval(left) != int(right):
            res[i] = 'X'
    return res
