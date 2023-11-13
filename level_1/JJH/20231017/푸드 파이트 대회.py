# 예상 시간 복잡도 O(n^2)
import math
def solution(food):
    answer = []
    for i in range(0,len(food)):
        for k in range(0,math.floor(food[i]/2)):
            answer.append(str(i))
    reverse = [answer[i] for i in range(len(answer)-1,-1,-1)]
    answer.append(str(0))
    answer = answer + reverse
    return ''.join(answer)
