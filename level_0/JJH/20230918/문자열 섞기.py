# 예상 시간 복잡도 : O(n) n : str1 + str 2 length
def solution(str1, str2):
    answer = []
    for i in range(0,len(str1+str2)):
        if i % 2 == 0:
            answer.append(str1[i//2])
        else:
            answer.append(str2[i//2])
    return ''.join(answer)
