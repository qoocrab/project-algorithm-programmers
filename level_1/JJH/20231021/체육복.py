def solution(n, lost, reserve):
    answer = 0
    lost.sort()
    reserve.sort()
    clothList = [1 for i in range(0, n)]
    for i in reserve:
        clothList[i-1] += 1
    for i in lost:
        clothList[i - 1] -= 1

    for i in range(0, n):
        if clothList[i] == 0:
            if i >= 1 and clothList[i - 1] == 2:
                clothList[i - 1] -= 1
                clothList[i] += 1
            elif i < n-1 and clothList[i + 1] == 2:
                clothList[i + 1] -= 1
                clothList[i] += 1
            else:
                pass
    answer = n - clothList.count(0)

    return answer

print(solution(5,[2,3,5],[2,3,4]))