def solution(numlist, n):
    if n in numlist:
        remain = numlist.copy()
        remain.remove(n)
        sortList = []
        sortList.append([n, 0])
    else:
        nearest, _ = findNearest(n, numlist)
        remain = numlist.copy()
        remain.remove(nearest)
        sortList = []
        sortList.append([nearest,_])
    while remain != []:
        nearest, diff = findNearest(n, remain)
        sortList.append([nearest,diff])
        remain.remove(nearest)

    for i in range(1,len(sortList)):
        for m in range(i, len(sortList)):
            if sortList[i][1] == sortList[m][1]:
                if sortList[i][0] < sortList[m][0]:
                    tmp = sortList[i]
                    sortList[i] = sortList[m]
                    sortList[m] = tmp

    return [sortList[i][0] for i in range(0,len(sortList))]

def findNearest(n, array):
    nearest = 100000
    for i in range(0, len(array)):

        if abs(n - nearest) > abs(array[i] - n):
            nearest = array[i]
    return nearest, abs(nearest - n)
