# 예상 시간 복잡도 O(1)
def solution(x):
    answer = True
    Sum = sum([int(str(x)[i]) for i in range(0,len(str(x)))])
    if x % Sum == 0:
        pass
    else:
        answer = False
    return answer
