def solution(a, b):
    answer = []
    if len(a) > len(b):
        diff = len(a) - len(b)
        loop = len(a)
        isABig = True
    else:
        diff = len(b) - len(a)
        loop = len(b)
        isABig = False
    roundNum = 0
    for i in range(loop-1, -1,-1):
        if isABig:

            if i - diff >= 0:
                aNum = int(a[i])
                bNum = int(b[i - diff])
                remain = (aNum + bNum + roundNum) % 10
                roundNum = (aNum + bNum + roundNum) // 10
                answer.append(str(remain))
            else:
                aNum = int(a[i])
                remain = (aNum + roundNum) % 10
                roundNum = (aNum + roundNum) // 10
                answer.append(str(remain))
        else:

            if i - diff >= 0:
                aNum = int(a[i - diff])
                bNum = int(b[i])
                remain = (aNum + bNum + roundNum) % 10
                roundNum = (aNum + bNum + roundNum) // 10
                answer.append(str(remain))
            else:
                bNum = int(b[i])
                remain = (bNum + roundNum) % 10
                roundNum = (bNum + roundNum) // 10
                answer.append(str(remain))
    if roundNum == 1:
        answer.append(str(roundNum))

    answer.reverse()
    return ''.join(answer)
