# 예상 시간복잡도: O(N)
def solution(myString):
    return ''.join(['l' if i<'l' else i for i in myString ])
