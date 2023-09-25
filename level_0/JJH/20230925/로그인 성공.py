# 예상 시간 복잡도 O(n) n db length
def solution(id_pw, db):
    answer = ''
    isFound = False
    for i in db:
        if i[0] == id_pw[0]:
            if i[1] == id_pw[1]:
                answer = 'login'
                isFound = True
                break
            else:
                answer = 'wrong pw'
                isFound = True
                break
    if not isFound:
        answer = 'fail'
    return answer
