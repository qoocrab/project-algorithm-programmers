# 예상 시간 복잡도 O(n) n string len
def solution(s):
    answer = True
    if len(s) == 4 or len(s) == 6:
        for i in s:
            if i.isdigit():
                pass
            else:
                answer = False
                break
    else:
        answer = False

    return answer
