# 예상 시간 복잡도 : O(n)
# [-1] --> list 역순!! 을 이용하면 쉽게 해결 가능
def solution(myString, pat):
    answer = ''
    String = myString
    index = 0
    i = 0
    while i >= 0:
        if pat in String:
            i = String.find(pat)
            index = index + i + 1
            String = String[i + 1:]
        else:
            break
    return myString[:index]
