# 예상 시간복잡도: O(n)
def solution(hp):
    answer = 0
    while hp > 0:
        if hp >= 5:
            hp = hp - 5
        elif hp < 5 and hp >= 3:
            hp = hp - 3
        elif hp < 3 and hp >= 1:
            hp = hp - 1
        else:
            break
        answer = answer + 1
    return answer
