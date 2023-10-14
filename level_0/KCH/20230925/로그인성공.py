# 예상 시간복잡도: O(N)
def solution(id_pw, db):
    DB = dict(db)
    InputID, InputPW = id_pw
    
    pw = DB.get(InputID, False)
    if pw:
        if InputPW == pw:
            return 'login'
        else: return 'wrong pw'
    return 'fail'
