# 예상 시간 복잡도 O(n^3)

def solution(keymap, targets):
    answer = []

    for i in targets:
        totalKeyPress = 0
        done = True
        for k in range(0, len(i)):
            keyPress = getKeyPress(i[k], keymap)
            if keyPress == 102:
                done = False
                break
            else:
                totalKeyPress += keyPress

        if not done:
            answer.append(-1)
        else:
            answer.append(totalKeyPress)
    return answer


def getKeyPress(key, keymap):
    keyPress = 101
    for i in keymap:
        if key in i:
            if keyPress > i.index(key):
                keyPress = i.index(key)
            if keyPress == 0:
                break
    return keyPress + 1
