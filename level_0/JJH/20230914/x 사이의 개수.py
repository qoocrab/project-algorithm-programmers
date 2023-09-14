# 예상 시간복잡도: O(m) m : String length
def solution(myString):
    answer = []
    list = myString.split('x')
    answer = [len(i) for i in list]
    return answer
