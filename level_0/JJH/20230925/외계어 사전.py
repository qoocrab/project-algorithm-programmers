# 예상 시간 복잡도 O(1)
def solution(spell, dic):
    answer = 2
    for i in dic:
        if len(i) != len(spell):
            continue
        else:
            status = True
            for m in spell:
                if m not in i:
                    status = False
                    break

            if status is True:
                answer = 1
                break
    return answer

print(solution(['z','d','x'],['def','dzx']))