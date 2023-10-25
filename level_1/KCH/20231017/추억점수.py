# 예상 시간복잡도: O(N)
def solution(name, yearning, photo):
    score_dict = dict()
    for i in range(len(name)):
        score_dict[name[i]] = yearning[i]
    
    op = lambda x: score_dict[x] if x in score_dict else 0
    res = []
    for case in photo: 
        res.append(sum([op(x) for x in case]))
    return res

#cf) dictionary = dict(zip(name,yearning))
