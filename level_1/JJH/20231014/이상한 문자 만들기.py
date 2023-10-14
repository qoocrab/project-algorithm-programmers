# 예상 시간 복잡도 O(n) n s'length
def solution(s):
    answer = []
    wordCount = -1
    for i in range(0, len(s)):
        if s[i] == ' ':
            wordCount = -1
            answer.append(' ')
        else:
            wordCount = wordCount + 1
            if wordCount % 2 == 0:
                answer.append(s[i].upper())
            else:
                answer.append(s[i].lower())

    return ''.join(answer)
