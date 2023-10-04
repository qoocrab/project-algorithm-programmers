# 예상 시간복잡도: O(N**2)
def solution(dots):
    incli = []
    for i in range(4):
        for j in range(i+1, 4):
            x1, y1 = dots[i]
            x2, y2 = dots[j]
            incli.append((x1-x2+0.1)/(y1-y2+0.1))
            
    return int(len(set(incli)) != len(incli))
