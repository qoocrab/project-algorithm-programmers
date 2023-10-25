# 예상 시간복잡도: O(NK), K: 각 옹알이 길이
def solution(babbling):
    pattern = ["aya", "ye", "woo", "ma"]
    res = 0
    for word in babbling:
        for i in range(len(pattern)):
            word = word.replace(pattern[i], str(i))
            if str(i)*2 in word: 
                break
                
        else:
            if set(word) - {'1', '2', '3', '0'}: 
                continue
            res += 1
    return res
