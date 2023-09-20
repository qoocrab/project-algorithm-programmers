# 예상 시간 복잡도 : O(n^2) n i~j number length
def solution(i, j, k):
    answer = 0
    for m in range(i,j+1):
        for l in range(0,len(str(m))):
            if str(k) == str(m)[l]:
                answer = answer + 1
            else:
                pass
    return answer
