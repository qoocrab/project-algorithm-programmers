# 예상 시간복잡도: O(n)
def solution(myString, pat):
    answer = 0
    convertMyString = ''
    for i in range(0,len(myString),1):
        if myString[i] == 'A':
            convertMyString = convertMyString + 'B'
        elif myString[i] == 'B':
            convertMyString = convertMyString + 'A'
        else:
            pass
    if convertMyString.find(pat) >= 0:
        answer = 1

    return answer
