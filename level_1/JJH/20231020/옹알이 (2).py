def solution(babbling):
    answer = 0
    availableList = ["aya", "ye", "woo", "ma"]
    for i in babbling:  # for all babbling
        String = i
        prevWord = -1
        while len(String) > 0:  # for one Babbling
            isAvailable = False
            for k in range(0, len(availableList)):  # if babbling is available
                if isWordInString(availableList[k], String):
                    if prevWord != k:
                        isAvailable = True
                        prevWord = k
                        break
                    else:
                        break

            if isAvailable:
                String = String[len(availableList[prevWord]):]
                if len(String) == 0:
                    answer = answer + 1
                    break
            else:
                break

    return answer


def isWordInString(word, string):
    result = True
    for i in range(0, min(len(word), len(string))):
        if string[i] == word[i]:
            pass
        else:
            result = False
            break
    return result

print(solution(["ayayeayayeaya"]))