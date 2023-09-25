# 예상 시간 복잡도 O(n) n picture length
def solution(picture, k):
    answer = []
    for i in picture:
        row=[]
        for m in i:
            for l in range(0,k):
                row.append(m)
        for l in range(0,k):
            answer.append(''.join(row))
    return answer
