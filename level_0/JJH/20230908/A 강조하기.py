# 예상 시간복잡도: O(n)
def solution(myString):
    answer = ''
    for i in myString:
        if i.isalpha():
            if i == 'a':
                answer = answer + 'A'
            else:
                if i != 'A':
                    answer = answer + i.lower()
                else:
                    answer = answer + i
        else:
            answer = answer + i.lower()

    return answer
